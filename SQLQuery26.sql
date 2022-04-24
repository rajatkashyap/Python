/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [number]
      ,[order_date]
      ,[cust_id]
      ,[salespserson_id]
      ,[amount]
  FROM [AdventureWorks2012].[Person].[orders]

  /****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [id]
      ,[name]
      ,[age]
      ,[salary]
  FROM [AdventureWorks2012].[Person].[salesperson]

  /****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [id]
      ,[name]
      ,[city]
      ,[industry_type]
  FROM [AdventureWorks2012].[Person].[customer]

  select name from [AdventureWorks2012].[Person].[salesperson] s
inner join (select count(*) cnt, [salespserson_id] from [AdventureWorks2012].[Person].[orders]  group by [salespserson_id] having count(*)>1)  o
on 
s.id=o.[salespserson_id]


  select name from [AdventureWorks2012].[Person].[salesperson] s
inner join [AdventureWorks2012].[Person].[orders] o
on s.id=o.[salespserson_id]
 group by name having count(*)>1

select count(*) cnt, [salespserson_id] from [AdventureWorks2012].[Person].[orders]  group by [salespserson_id] having count(*)>1)  o
on 
s.id=o.[salespserson_id]



  a. The names of all salespeople that have an order with Samsonic. 

  select s.name
  from  [AdventureWorks2012].[Person].[salesperson] s,
    [AdventureWorks2012].[Person].[orders] o,
	 [AdventureWorks2012].[Person].[customer] c
	 where 
	 s.id=o.salespserson_id
	 and o.cust_id=c.id
	 and
	 c.name='Samsonic'

select o.salespserson_id from   [AdventureWorks2012].[Person].[orders] o
where not exists(select 1 from  [AdventureWorks2012].[Person].[customer] c where o.cust_id=c.id and c.name='Samsonic')


select name from [AdventureWorks2012].[Person].[salesperson] s
where not exists(
select  o.salespserson_id from[AdventureWorks2012].[Person].[orders] o, [AdventureWorks2012].[Person].[customer] c where o.cust_id=c.id
and c.name='Samsonic' and s.id=o.salespserson_id)



select name from [AdventureWorks2012].[Person].[salesperson] s inner join
(select salespserson_id,count(*) cnt  from [AdventureWorks2012].[Person].[orders] o group by salespserson_id having count(*)>1) o
on s.id=o.salespserson_id


select * from [AdventureWorks2012].[Person].[salesperson]
where salary>=100000

select emplyee_anme from employee e, 
(select max(salary) sal, dpeatrtmenId from employee group by departemnt_id) x
where e.dept_id=x.dept_id


select * from [AdventureWorks2012].[Person].[salesperson] where salary =
(
select max(salary) from [AdventureWorks2012].[Person].[salesperson]
where salary<(select max(salary) from [AdventureWorks2012].[Person].[salesperson]))

select * from [AdventureWorks2012].[Person].[salesperson] where salary =
(
select max(salary) from [AdventureWorks2012].[Person].[salesperson]
where salary<(select max(salary) from [AdventureWorks2012].[Person].[salesperson]))


select * from [AdventureWorks2012].[Person].[salesperson] s1 where 2=
(select count(*) from [AdventureWorks2012].[Person].[salesperson] s2 where s2.salary>=s1.salary)

day fruit no
today apple 10
today oranges 20

create table fruits
(sell_date date,
fruit char(1), 
sold int)

insert into fruits values(getdate(),'a', 20)
insert into fruits values(getdate(),'o', 9)

select *  from fruits


select no_a-no_o,a.sell_date
from
(select sold no_a,sell_date   from fruits a where fruit= 'a' and sell_date=cast(getdate() as date))a,
(select sold no_o,sell_date   from fruits b where fruit= 'o' and sell_date=cast(getdate() as date))b
where a.sell_date=b.sell_date


select sold from  fruits a where fruit= 'a' and sell_date=cast(getdate() as date)
except
select sold from  fruits a where fruit= 'o' and sell_date=cast(getdate() as date)

select sell_date,sum(case when fruit= 'a' then sold else 0 end)-sum(case when fruit= 'o' then sold else 0 end)
from 
fruits
group by sell_date





  select * from [AdventureWorks2012].[Person].[AddressType] a
  where exists (select 1 from [AdventureWorks2012].[Person].[BusinessEntityAddress] b where b.AddressTypeID=a.AddressTypeID)






  /****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [id]
      ,[t1Id]
      ,[someData]
  
   FROM [AdventureWorks2012].[Person].[t2]

   use [AdventureWorks2012]


   SELECT    t1.* 
FROM    [Person].t1 t1
        JOIN [Person].t2 t2 ON t1.id = t2.t1Id

		SELECT    t1.* 
FROM    [Person].t1  t1 
WHERE    t1.id IN (SELECT someIntCol  FROM [Person].t2 t2 )