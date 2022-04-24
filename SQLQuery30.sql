/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [BusinessEntityID]
      ,[NationalIDNumber]
      ,[LoginID]
      ,[OrganizationNode]
      ,[OrganizationLevel]
      ,[JobTitle]
      ,[BirthDate]
      ,[MaritalStatus]
      ,[Gender]
      ,[HireDate]
      ,[SalariedFlag]
      ,[VacationHours]
      ,[SickLeaveHours]
      ,[CurrentFlag]
      ,[rowguid]
      ,[ModifiedDate]
  FROM [AdventureWorks2012].[HumanResources].[Employee]

  select * from [AdventureWorks2012].[HumanResources].[Employee]
  where JobTitle like 'Production Technician - WC[0-9][0-9]'
  and JobTitle='Production Technician - WC10'

  select * from [AdventureWorks2012].[HumanResources].[Employee]
  where JobTitle like 'Production Technician - WC_0'

    select * from [AdventureWorks2012].[HumanResources].[Employee]
  where JobTitle like '[PSET]%'

  select jobtitle  --,OrganizationLevel
,count(*)
    from [AdventureWorks2012].[HumanResources].[Employee]
	group by jobtitle
	
	  select OrganizationLevel,jobtitle
,count(*)
    from [AdventureWorks2012].[HumanResources].[Employee]
	group by OrganizationLevel,jobtitle


	
  select jobtitle,OrganizationLevel
,count(*)
    from [AdventureWorks2012].[HumanResources].[Employee]
	  group by grouping sets(jobtitle,OrganizationLevel)




  
  select OrganizationLevel,gender
,count(*)
  from [AdventureWorks2012].[HumanResources].[Employee]
  group by rollup(OrganizationLevel,gender)


   select OrganizationLevel,gender
,count(*)
  from [AdventureWorks2012].[HumanResources].[Employee]
  group by cube(OrganizationLevel,gender)


  
    select * from [AdventureWorks2012].[HumanResources].[Employee]
	order by OrganizationLevel
	fetch first 10  