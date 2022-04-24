/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [id]
      ,[name]
      ,[salary]
      ,[dept]
  FROM [AdventureWorks2012].[Person].[testperson]

  select * from [AdventureWorks2012].[Person].[testperson]
  where id in (select id from [AdventureWorks2012].[Person].[testperson] where salary!=100)

  select max(salary) from [AdventureWorks2012].[Person].[testperson]
  where salary not in (select max(salary) from  [AdventureWorks2012].[Person].[testperson])

  select distinct salary from [AdventureWorks2012].[Person].[testperson] t1
  where   1=(select count(distinct salary) from [AdventureWorks2012].[Person].[testperson] t2 where t2.salary>t1.salary)


select count(distinct salary) from [AdventureWorks2012].[Person].[testperson] t2 where 100 <=t2.salary
select count(distinct salary) from [AdventureWorks2012].[Person].[testperson] t2 where 200 <t2.salary

   select max(salary) from [AdventureWorks2012].[Person].[testperson]
  where salary!=(select max(salary) from  [AdventureWorks2012].[Person].[testperson])

  select top 1 salary from [AdventureWorks2012].[Person].[testperson]
  where salary!=(select top 1 salary from [AdventureWorks2012].[Person].[testperson])