/****** Script for SelectTopNRows command from SSMS  ******/
select name,score, min(cnt) 
from (

SELECT name,score,1 as cnt
  FROM [AdventureWorks2012].[Person].student
  
  union all
  SELECT name,score,2 as cnt
  FROM [AdventureWorks2012].[Person].student3
  
  )a
  group by name,score


  select user_id, training_id , traianing_date
  from training_details
  grouped by 
  user_id, training_id , traianing_date
  having count(*)>1
  order by trainigmg_date desc

  alter table [AdventureWorks2012].[Person].student3
  add age int

  select * from [AdventureWorks2012].[Person].student
  select * from [AdventureWorks2012].[Person].student3
  
  update [AdventureWorks2012].[Person].student
  set id=3 where score=600


  select * from 
  [AdventureWorks2012].[Person].student
s  left outer join 
[AdventureWorks2012].[Person].student3 s1
on s.id=s1.id

  select *,(select count(*) from [AdventureWorks2012].[Person].student a where score>=[AdventureWorks2012].[Person].student.score) from 
  [AdventureWorks2012].[Person].student


  select * from [AdventureWorks2012].[Person].student b

where 2=(select count(*) from [AdventureWorks2012].[Person].student a where a.score>=b.score)

 select * from [AdventureWorks2012].[Person].student b
select * from [AdventureWorks2012].[Person].student b
where (select count(*) from [AdventureWorks2012].[Person].student a where a.id<b.id)<3


select * from salesperson s
inner join (select count(*), salesperson_id from orders  group by salesperson_id having count(*)>1)  o
on 
s.id=o.salesperson_id

