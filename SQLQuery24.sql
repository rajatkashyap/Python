/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [ID]
      ,[Name]
      ,[Age]
      ,[Salary]
  FROM [AdventureWorks2012].[HumanResources].[Salesperson]

  CREATE table [AdventureWorks2012].[HumanResources].likes
(
    userid int not null,
    pageid int not null
)

CREATE  table [AdventureWorks2012].[HumanResources].friends
(
    userid int not null,
    friendid int not null
)


insert into [AdventureWorks2012].[HumanResources].likes VALUES
(1, 101), 
(1, 201),
(2, 201), 
(2, 301);

insert into [AdventureWorks2012].[HumanResources].friends VALUES (1, 2);

select f.userid, l.pageid,l1.userid,l1.pageid 
from [AdventureWorks2012].[HumanResources].likes l
inner join [AdventureWorks2012].[HumanResources].friends f
on f.friendid=l.userid
left join [AdventureWorks2012].[HumanResources].likes l1
on f.userid=l1.userid
and l.pageid=l1.pageid
where l1.pageid is null


