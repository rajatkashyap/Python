/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [T1ID]
      ,[Name]
  FROM [AdventureWorks2012].[Person].[T1]

  SELECT TOP 1000 [T2ID]
      ,[T1ID]
      ,[Name]
  FROM [AdventureWorks2012].[Person].[T2]


  select * 
  from [AdventureWorks2012].[Person].[T2] t2
  left outer join [AdventureWorks2012].[Person].[T1]
  on t2.t1id=t1.t1id

  insert into  [AdventureWorks2012].[Person].[T2_TEMP] values (1,NULL,T2Text2)
   insert into  [AdventureWorks2012].[Person].[T2_TEMP] values (2,2,T2Text3)
  select t1id,name,coalesce(t1id,name,'UNK') from [AdventureWorks2012].[Person].[T2] t2
