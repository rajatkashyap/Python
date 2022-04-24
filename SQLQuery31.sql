/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [id]
      ,[name]
      ,[salary]
      ,[dept]
  FROM [AdventureWorks2012].[Person].[testperson]

   
  select id,name,salary,dept from [AdventureWorks2012].[Person].[testperson] t1
  where salary>
  (select avg(salary) from [AdventureWorks2012].[Person].[testperson] t2
  where t1.dept=t2.dept)

  select id,name,t1.dept from [AdventureWorks2012].[Person].[testperson] t1,
  (select dept,avg(salary)avgsal from [AdventureWorks2012].[Person].[testperson] group by dept) t2
  where t1.dept=t2.dept
  and t1.salary>t2.avgsal


  id	name	dept
2		b	101
6		c1	102
9		a	103