create view view_1 as
select articles.slug as slug, count(log.path) as num from
log join articles
on log.path = ('/article/' || articles.slug)
group by slug
order by num desc;

create view view_2 as
select articles.title, num, articles.author as author from
articles join view_1
on articles.slug = view_1.slug;

create view status200 as
select distinct(date_trunc('day',time)) as time, count(time) as status
from log
where status like '2%'
group by date_trunc('day',time)
order by time asc;

create view status404 as
select distinct(date_trunc('day',time)) as time, count(time) as status
from log
where status like '4%'
group by date_trunc('day',time)
order by time asc;

create view view_3 as
select status200.time as time,
status200.status as ok,
status404.status as notok
from status200 join status404
on status200.time = status404.time;
