/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [SalesOrderID]
      ,[SalesOrderDetailID]
      ,[CarrierTrackingNumber]
      ,[OrderQty]
      ,[ProductID]
      ,[SpecialOfferID]
      ,[UnitPrice]
      ,[UnitPriceDiscount]
      ,[LineTotal]
      ,[rowguid]
      ,[ModifiedDate]
  FROM [AdventureWorks2012].[Sales].[SalesOrderDetail]

  create table [AdventureWorks2012].person.testperson
  (
  id int,
  name varchar(20),
  salary int,
  dept int)

  insert into [AdventureWorks2012].person.testperson values (1, 'a',100,101)
  insert into [AdventureWorks2012].person.testperson values (2, 'b',200,101)
insert into [AdventureWorks2012].person.testperson values (3, 'c',150,101)
insert into [AdventureWorks2012].person.testperson values (4, 'a1',100,102)
insert into [AdventureWorks2012].person.testperson values (5, 'b1',110,102)
insert into [AdventureWorks2012].person.testperson values (6, 'c1',120,102)
insert into [AdventureWorks2012].person.testperson values (7, 'a',200,103)
insert into [AdventureWorks2012].person.testperson values (8, 'a',200,103)
  insert into [AdventureWorks2012].person.testperson values (9, 'a',230,103)

  use  [AdventureWorks2012]
  
  select * from  [AdventureWorks2012].person.testperson 

  select dept,salary,first_value(salary)  over(partition by dept order by salary rows between 1 preceding and current row  ),
  last_value(salary)  over(partition by dept order by salary rows between current row  and 1 following)
  from person.testperson 
