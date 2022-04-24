/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [BusinessEntityID]
      ,[AddressID]
      ,[AddressTypeID]
      ,[rowguid]
      ,[ModifiedDate]
  FROM [AdventureWorks2012].[Person].[BusinessEntityAddress]

  use [AdventureWorks2012]

  SELECT  *
FROM    Person.BusinessEntity be
WHERE   NOT EXISTS ( SELECT 1
                     FROM   Person.BusinessEntityAddress bea
                     WHERE  bea.BusinessEntityID = be.BusinessEntityID );


select * from Person.BusinessEntityAddress where BusinessEntityID=291

select * from  Person.BusinessEntity be left outer join Person.BusinessEntityAddress bea
on  bea.BusinessEntityID = be.BusinessEntityID
where  bea.BusinessEntityID is null


 Id  Name  Sex  Salary
1   A     m    2500
2   B     f    1500
3   C     m    5500
4   D     f    500


update salaries
set sex=(case when Sex='m' then 'f' else 'm' end) 
from salaries a 
where salaries.id=a.id

  select *,(select count(*) from [AdventureWorks2012].[Person].student a where score>=[AdventureWorks2012].[Person].student.score) rnk from 
  [AdventureWorks2012].[Person].student
