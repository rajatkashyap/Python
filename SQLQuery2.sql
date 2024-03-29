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

  select salesorderid,[OrderQty], avg( [OrderQty]) over (partition by salesorderid order by [OrderQty] )
  from [AdventureWorks2012].[Sales].[SalesOrderDetail]


  select salesorderid,linetotal, count( linetotal) over (partition by salesorderid order by linetotal )
  from [AdventureWorks2012].[Sales].[SalesOrderDetail]

  select sum(distinct linetotal)
   from [AdventureWorks2012].[Sales].[SalesOrderDetail]
   group by  salesorderid

  select * from departments where exists (select 1 from employees where departments.manager_id=employees.employee_id and salary>20000)


  select * from departments where manager_id in (select employee_id from employees where salary>20000)


  select candidate_name, count(*)
  from candidate_votes v, candidates c
  where c.candidate_id=v.candidate_id
  group by v.candidate_id
  order by count(*) desc limit 1


  SELECT   candidates.*
FROM     candidates JOIN candidate_votes USING (candidate_id)
GROUP BY candidate_id
HAVING   COUNT(*) = (
  SELECT   COUNT(*) votes
  FROM     candidate_votes
  GROUP BY candidate_id
  ORDER BY votes DESC
  LIMIT    1
)