/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [Number]
      ,[order_date]
      ,[cust_id]
      ,[salesperson_id]
      ,[Amount]
  FROM [AdventureWorks2012].[HumanResources].[Orders]


  select salesperson_id, rank() over (order by amount desc) from 
  [AdventureWorks2012].[HumanResources].[Orders]

  select s.name

  FROM [AdventureWorks2012].[HumanResources].[Orders] o	
  inner join  [AdventureWorks2012].[HumanResources].salesperson s
  on o.[salesperson_id]=s.id
  inner join [AdventureWorks2012].[HumanResources].customer c
  on o.cust_id=c.id
  where c.name='Samsonic'

  select * from [AdventureWorks2012].[HumanResources].salesperson s
  where   not exists(
  select [salesperson_id]
  from  [AdventureWorks2012].[HumanResources].[Orders] o
  inner join [AdventureWorks2012].[HumanResources].customer c
  on o.cust_id=c.id
   where c.name='Samsonic' 
   and o.[salesperson_id]=s.id)

   select s.* from [AdventureWorks2012].[HumanResources].salesperson s left outer join
   (
select [salesperson_id]  from  [AdventureWorks2012].[HumanResources].[Orders] o
  inner join [AdventureWorks2012].[HumanResources].customer c
  on o.cust_id=c.id
   where c.name='Samsonic') o
   on
   s.id=o.[salesperson_id]
   where o.[salesperson_id] is  null

   select name from [AdventureWorks2012].[HumanResources].salesperson s
   inner join 
   (
   select count(*) cnt, [salesperson_id]
   from [AdventureWorks2012].[HumanResources].[Orders] 
   group by [salesperson_id]
   having count(*)>1
   )a
   on s.id=a.[salesperson_id]


      select name from [AdventureWorks2012].[HumanResources].salesperson s
   inner join 
   (
   select sum(Amount) amt, [salesperson_id]
   from [AdventureWorks2012].[HumanResources].[Orders] 
   group by [salesperson_id]
   having sum(Amount)>1400
   )a
   on s.id=a.[salesperson_id]


   select min(order_date), max(order_date)
   from  [AdventureWorks2012].[HumanResources].[Orders] o
   inner join [AdventureWorks2012].[HumanResources].customer c
   on o.cust_id=c.id
   where c.name='Samsony'


   insert into   [AdventureWorks2012].[HumanResources].salesperson 
   values (12,'Jon',NULL,NULL)

   select * from [AdventureWorks2012].[HumanResources].salesperson 



   select avg(salary), sum(salary)/count(*) from [AdventureWorks2012].[HumanResources].salesperson 

   select * from [AdventureWorks2012].[HumanResources].salesperson 
   where salary>(select avg(salary) from [AdventureWorks2012].[HumanResources].salesperson )

    select * from [AdventureWorks2012].[HumanResources].salesperson s1
	inner join
	(select avg(salary) sal from [AdventureWorks2012].[HumanResources].salesperson) s2
	on
	s1.salary>s2.sal
   

   select * from [AdventureWorks2012].[HumanResources].salesperson s1
   where exists (select avg(salary) from [AdventureWorks2012].[HumanResources].salesperson s2 where s1.id=s2.id and s1.salary>avg(salary))

   

  select col1, coalesce(col2,'UNKNOWN') from [AdventureWorks2012].[Person].[Test1]