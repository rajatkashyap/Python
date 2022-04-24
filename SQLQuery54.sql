/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [BusinessEntityID]
      ,[RateChangeDate]
      ,[Rate]
      ,[PayFrequency]
      ,[ModifiedDate]
  FROM [AdventureWorks2012].[HumanResources].[EmployeePayHistory]

  CREATE TABLE [dbo].[OranApps](
    [OrderDate] [date] NULL,
    [Name] [nchar](10) NULL,
    [Sold] [int] NULL
) 
insert into [dbo].[OranApps] values('2019-01-02', 'Oranges', 10)
insert into [dbo].[OranApps] values('2019-01-02','Apples', 5)
insert into [dbo].[OranApps] values('2019-01-03','Oranges', 20)
insert into [dbo].[OranApps] values('2019-01-03', 'Apples', 25)


select * from [dbo].[OranApps]


select o.OrderDate,
a.Sold-o.Sold as diff
 from

[dbo].[OranApps] o
inner join [dbo].[OranApps] a
on o.OrderDate=a.OrderDate
 where o.Name='Oranges'
 and a.Name='Apples'


 select *
 from

[dbo].[OranApps] o
inner join [dbo].[OranApps] a
on o.OrderDate=a.OrderDate
 where o.Name='Oranges'
 and a.Name='Apples'

 create table customer(cusID int, cusName VARCHAR(10));

insert into customer values(1, 'Ali');
insert into customer values(2, 'Moh');
insert into customer values(3, 'Abdo');

create table item(cusID int, itemName VARCHAR(10));

insert into item values(1, 'A');
insert into item values(1, 'B');
insert into item values(2, 'A');
insert into item values(2, 'B');
insert into item values(3, 'A');

select count(c.cusname)
from customer c inner join
(select cusID, count(distinct itemName) cnt
from item
group by cusID
having count(distinct itemName)=2)i
on c.cusid=i.cusid