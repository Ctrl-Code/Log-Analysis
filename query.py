#!/usr/bin/env python3

import psycopg2


def execute_query(query):
    conn = psycopg2.connect("dbname=news")
    curs = conn.cursor()
    curs.execute(query)
    ans = curs.fetchall()
    curs.close()
    conn.close()
    return ans


def print_top_articles():
    print("Que 1:What are the most popular three articles of all time?")
    query = ''' SELECT title, num FROM view_2
                ORDER BY num DESC
                LIMIT 3;'''
    result = execute_query(query)
    for title, num in result:
        print("Sol  :" + title + " - " + str(num) + " views")
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")


def print_top_authors():
    print("Que 2:Who are the most popular article authors of all time?")
    query = ''' SELECT authors.name AS author, sum(num) AS views
                FROM view_2 JOIN authors
                ON view_2.author = authors.id
                GROUP BY authors.name
                ORDER BY views DESC;'''
    result = execute_query(query)
    for author, views in result:
        print("Sol  :" + author + " - " + str(views) + " views")
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")


def print_errors_over_one():
    print("Que 3:On which days did more than '1%' of requests lead to errors?")
    query = ''' SELECT to_char(time,'Mon DD,YYYY - ') AS date,
                ROUND(CAST(percentage AS NUMERIC),2) AS percentage FROM
                (   SELECT time,
                    ( CAST(notok * 100 AS REAL) / CAST((ok+notok) AS REAL))
                    AS percentage
                    FROM view_3
                    ORDER BY time )
                AS table_alias
                WHERE percentage > 1.0;'''
    result = execute_query(query)
    for date, percentage in result:
        print("Sol  : " + date + str(percentage) + "%" + " errors")


if __name__ == "__main__":
    print_top_articles()
    print_top_authors()
    print_errors_over_one()
