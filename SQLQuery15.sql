/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [emp_id]
      ,[name]
      ,[mgr_id]
      ,[salary]
  FROM [AdventureWorks2012].[HumanResources].[emp]

  create table [AdventureWorks2012].[HumanResources].Orders
  (
  Number int ,
  order_date date,
  cust_id int,
  salesperson_id int,
  Amount int)

  insert into [AdventureWorks2012].[HumanResources].Customer values(4, 'Samsony','Jackson', 'B')