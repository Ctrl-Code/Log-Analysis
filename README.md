# Log Analysis

This project answers the below mentioned 3 questions asked for in the project:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

***

## Pre-Requisites

Any Linux System (Ubuntu Prefered) with:

- [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file. ( Extract the zip file to get 'newsdata.sql'.)
- `PostGreSQL` installed
- `Python3` with `psycopg2` module installed.

***

## Setup

1. Create database named `news`.
    - Open up terminal and type in below command. This will run 'psql' as user postgres
    ``` bash
    sudo -u postgres psql
    ```
    - Now the prompt will change to 'postgres=#'. Type in below SQL command to create a database named 'news'.
    ``` SQL
    CREATE DATABASE news;
    ```

2. Import the extracted SQL file `newsdata.sql` ( Dowload link given in pre-requisites above).
    - Change to the current working directory of 'psql' to directory containing 'newsdata.sql'. Below given path assumes that the username is 'vm' and the sql file is kept on Desktop. Change below given path ie.'/home/vm/Desktop' accordingly. `\cd` here is psql meta command to change psql working directory.
    ``` PSQL
    \cd /home/vm/Desktop
    ```
    - Connect to the created database 'news' in step 1 above using 'psql' meta command - `\c` as shown below. The prompt will change to 'news=#'.
    ``` PSQL
    \c news
    ```
    - Below given 'psql' meta command - `\i` will import the file in database 'news'. Ignore errors regarding 'vagrant'. Wait till prompt returns back to 'news=#'.
    ``` PSQL
    \i newsdata.sql
    ```

3. Setup `DATABASE VIEWS` used in this project by importing `views.sql` file included here in the project directory. For this copy the file 'views.sql' it to the location as of 'newsdata.sql' and then running the below given command.

    ``` PSQL
    \i views.sql
    ```

***

## Running the file

Run the python file named `query.py` in the project directory in the terminal using the below given command.

``` bash
sudo -u postgres python3 query.py
```

Incase there occurs some error while executing above command see that everyone has 'read' permissions for file 'query.py'.

***

## Acknowledgements

This project is one of the series of projects of Udacity's Full Stack Nano Degree Course. The file `newsdata.sql` is provided by `Udacity`.