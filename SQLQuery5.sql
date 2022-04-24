/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [id]
      ,[name]
      ,[age]
      ,[salary]
  FROM [AdventureWorks2012].[Person].[salesperson]

  select max(salary) from [AdventureWorks2012].[Person].[salesperson]
where salary<(
  select max(salary) from [AdventureWorks2012].[Person].[salesperson]
where salary<( select max(salary) from [AdventureWorks2012].[Person].[salesperson]))

select * from 
(
select name,salary, dense_rank() over(order by salary desc) rnk
 FROM [AdventureWorks2012].[Person].[salesperson]
 )a
 where rnk=3

 SELECT TOP 1000 [id]
      ,[name]
      ,[age]
      ,[salary]
  FROM [AdventureWorks2012].[Person].[salesperson]
  SELECT COUNT(DISTINCT Salary) FROM [AdventureWorks2012].[Person].[salesperson] p WHERE 14000<=p.Salary

 SELECT name, Salary FROM [AdventureWorks2012].[Person].[salesperson] e WHERE 5=(SELECT COUNT(DISTINCT Salary) FROM [AdventureWorks2012].[Person].[salesperson] p WHERE e.salary<=p.Salary)

 select name, salary from [AdventureWorks2012].[Person].[salesperson] s where 3=(select count(distinct salary) from [AdventureWorks2012].[Person].[salesperson] s2 where s2.salary>=s.salary)


 select * from
 (select max(salary) s1 from [AdventureWorks2012].[Person].[salesperson]) a,
 (select max(salary) sal2 from [AdventureWorks2012].[Person].[salesperson]) b
 where s1=sal2

 select top 1 salary from (select top 2 salary from [AdventureWorks2012].[Person].[salesperson] order by salary desc)a order by salary

 select * from [AdventureWorks2012].[Person].[salesperson] 


 select * from emp e,departments d
where e.dept_id=d.dept_id
 and d.max_salary=40k 


 create table acceptance
 (
 accpt_id int,
 req_id int,
 sender_id int
 )

 update requests
 set req_id=2 where sender_id=104

insert into acceptance values(1,1,101)
insert into acceptance values(4,4,103)
insert into acceptance values(5,3,102)


select * from requests   r  left outer join acceptance a
on a.req_id=r.req_id
select * from acceptance

--find the acceptance rate
--assume request expires 10 days after request


select sum(case when a.accpt_id is null then 1 else 0 end),
count(r.req_id) ,
cast((sum(case when a.accpt_id is not null then 1 else 0 end)/(1.0*count(r.req_id))) as float) accet_rate
from requests r
  left outer join acceptance a
on a.req_id=r.req_id
where datediff(day,sent_date,getdate())>10


select right('abc',1) from acceptance


you have a table where you have date, user_id, song_id and count. 
It shows at the end of each day how many times in her history a user has listened to a given song. So count is cumulative sum.
You have to update this on a daily basis based on a second table that records in real time when a user listens to a given song. 
Basically, at the end of each day, you go to this second table and pull a count of each user/song combination and then add this count to the first table that has the lifetime count.

select user_id, sum(song_id)
from 
(
select  user_id, song_id from history 
union 
select user_id, song_id from current
)
group by user_id


select * from song_hist  h
full outer join curtrn c on 
user_id and song_id 


create table song_curr
(
 user_id int, song_id int, dt date)
 insert into song_curr values (1,101, getdate())
 insert into song_curr values (2,102, getdate())
insert into song_curr values (6,106, getdate())

insert into song_hist values (4,104, getdate())
 insert into song_hist values (5,105, getdate())


 update song_hist 
 set song_hist.count=x.tot
 from
 ( select user_id,song_id, sum(count) tot
 from(
 select  user_id, song_id, count from song_hist 
 union all
select user_id, song_id, 1 as count from song_curr
)a
group by user_id,song_id
)
x
where song_hist.user_id=x.user_id
and song_hist.song_id=x.song_id


select * from song_hist
select * from song_curr

delete from song_hist where dt is null

 insert into song_curr values (1,101, getdate())
 insert into song_curr values (2,102, getdate())
insert into song_curr values (6,106, getdate())
insert into song_curr values (8,108, getdate())



 merge into song_hist 
 using 
 ( select user_id,song_id,dt, sum(count) tot
 from(
 select  user_id, song_id,dt, count from song_hist 
 union all
select user_id, song_id,dt, 1 as count from song_curr
)a
group by user_id,song_id,dt
)x
on (song_hist.user_id=x.user_id and song_hist.song_id=x.song_id)
WHEN MATCHED THEN
update set song_hist.count=x.tot,song_hist.dt=x.dt
when not matched then
insert (user_id, song_id,dt,count)
     VALUES (x.user_id,x.song_id,x.dt,1);
 
 
 
 set song_hist.count=x.tot
 from
 ( select user_id,song_id, sum(count) tot
 from(
 select  user_id, song_id, count from song_hist 
 union all
select user_id, song_id, 1 as count from song_curr
)a
group by user_id,song_id
)
x
where song_hist.user_id=x.user_id
and 

drop table user_friends

create table user_friends
(
user_id int,
friend_id int)

create table user_likes
(
user_id int,
page_id int)

insert into user_friends values (1,10),(1,21),(1,30),(2,10),(2,21),(2,50)
insert into user_likes values (30,1001), (1,1001),(1,1002),(21,2001),(30,5001),(2,3001),(50,7001)

select * from user_friends
select * from user_likes
 select * from user_friends u inner join user_likes l on u.friend_id=l.user_id 

select user_id, page_id as recc_page_id

select u.user_id,page_id from user_likes l,user_friends u where u.friend_id=l.user_id 
 and l.page_id not in (select page_id from user_likes where user_id=u.user_id)


 select * from user_friends u inner join user_likes l on u.friend_id=l.user_id 
 left outer join user_likes x on u.user_id=x.user_id and l.page_id=x.[page_id]
 where x.page_id is null



 and  exists (select page_id from user_likes where user_id!=u.user_id)


 select post_id, comment_count
 from
 submission s,
 submission s1
 where 
 s.submission_id=s1.parent_id
 where s.parent_id is null


 create table Submissions 
 (submission_id int,
 body char(20),
 parent_id int)

 insert into Submissions values (1,null,null),(2,null,1),(3,null,nUll),(4,null,1),(5,null,1), (6,null,3)


 select * from submissions



 select s1.submission_id,  count(s2.submission_id) comment_count
 from submissions s1,
 submissions s2
 where s1.submission_id=s2.parent_id
 and s1.parent_id is null
 group by s1.submission_id


 SELECT comment_counts.n_comments, count(distinct comment_counts.submission_id)
 from
(
select s1.submission_id, COUNT (DISTINCT s2.parent_id) as n_comments
from submissions s1
full OUTER join submissions s2
on s1.submission_id = s2.parent_id
group by s1.submission_id) comment_counts
GROUP BY comment_counts.n_comments



select f.user_id, l.page_id,r.page_id
from user_friends f
join user_likes l ON l.user_id = f.user_id
LEFT JOIN user_likes r ON (r.user_id = f.user_id AND r.page_id = l.page_id)
where r.page_id IS NULL;





data question:
dialoglog
(userid int
appid int
type char , a flag either "imp" or "click"
ds timestamp
)

How would you access the quality of app?
How to compute click-through rate (in mySQL)

