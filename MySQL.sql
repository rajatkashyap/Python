select DEPARTMENT_NAME,FIRST_NAME,last_name,HIRE_DATE, SALARY
from departments d,employees e where
d.MANAGER_ID=e.EMPLOYEE_ID and
 DATEDIFF(now(),HIRE_DATE)/365>15


select first_name,last_name from employees where department_id =(select department_id from departments where department_name='IT');

select e.first_name,e.last_name from employees e,departments d,locations l, employees m 
where 
e.MANAGER_ID =m.EMPLOYEE_ID and
m.DEPARTMENT_ID =d.DEPARTMENT_ID  
and d.LOCATION_ID =l.LOCATION_ID and l.country_id='US';

 where department_id in (select department_id from departments where

Write a query to find the names (first_name, last_name) of the employees who have a manager who works for a department based in the United States.


select e.first_name,e.last_name from employees e
where exists(select manager_id from employees where e.manager_id =EMPLOYEE_ID )

select e.first_name,e.last_name from employees e where lower(first_name) like '%b%c%'

select e.first_name,e.last_name from employees e where job_id in ('PU_CLERK','IT_PROG') and salary not in (4500,10000,15000)


   



Write a query to find the names (first_name, last_name) of the employees who have a manager who works for a department based in the United States.


select distinct e.first_name,e.last_name from employees e, 
(select manager_id from employees) m
where m.MANAGER_ID =e.EMPLOYEE_ID 


SELECT first_name, last_name   
FROM employees e  where exists (select 1 from employees where manager_id =e.EMPLOYEE_ID);

SELECT first_name, last_name   
FROM employees e,(select avg(salary) avg_sal from employees) e1
where e.salary>e1.avg_sal;
 
SELECT first_name, last_name  , salary
FROM employees e,jobs j
where e.salary=j.MIN_SALARY
and e.job_id=j.job_id;

SELECT first_name, last_name  ,salary
FROM employees e,(select avg(salary) avg_sal from employees) e1,departments d
where e.salary>e1.avg_sal
and e.department_id=d.department_id and d.department_name like 'IT%';


SELECT first_name, last_name  ,salary
FROM employees e where e.salary>(select salary from employees where LAST_NAME='Bell');

mysql> SELECT * FROM employees
    -> WHERE salary >
    -> ALL(SELECT avg(salary)FROM employees GROUP BY department_id);
	
SELECT first_name, last_name  ,salary FROM employees e
where salary>(select max(salary) from employees where JOB_ID = 'SH_CLERK');

SELECT first_name, last_name  FROM employees e where not exists(select 1 from employees where manager_id=e.employee_id)

SELECT first_name, last_name,salary  FROM employees e where exists(select 1 from employees where DEPARTMENT_ID=e.DEPARTMENT_ID and e.salary>)

SELECT first_name, last_name,salary  FROM employees e,
(select DEPARTMENT_ID,avg(salary) avg_sal from employees
group by DEPARTMENT_ID) d
where e.department_id=d.department_id
and e.salary>d.avg_sal


select e.first_name, e.last_name, d.department_name, e1.salary
from employee e, employee e1
where e1.manager_id=e.employee_id
and e1.department_id=d.department_id
and 



select first_name, last_name from employees e where salary>(select avg(salary) from employees where department_id=e.department_id)	

select * from employees e where 4=(select count(distinct(salary)) from employees where salary>e.salary);
select * from employees e where 5=(select count(distinct(salary)) from employees where salary>=e.salary);

select distinct salary from employees e where 4=(select count(distinct(salary)) from employees where salary<=e.salary);

select   * from employees order by employee_id desc limit 10

-- 3 Top salaries
select distinct salary from employees e where (select count(distinct(salary)) from employees where salary>=e.salary) in (1,2,3) ;

SELECT DISTINCT salary   
FROM employees a   
WHERE 3 >= (SELECT COUNT(DISTINCT salary)   
FROM employees b   
WHERE b.salary >= a.salary)   
ORDER BY a.salary DESC;  

-- 3 Min salaries
select distinct salary from employees e where (select count(distinct(salary)) from employees where salary<=e.salary) in (1,2,3) ;

SELECT DISTINCT salary   
FROM employees a   
WHERE 3 >= (SELECT COUNT(DISTINCT salary)   
FROM employees b   
WHERE b.salary <= a.salary)   
ORDER BY a.salary DESC;  

select manager_id, min(salary)
from employees where manager_id!=0 group by manager_id;

select job_id,max(salary) from employees
group by job_id 
having max(salary)>4000



/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [T2ID]
      ,[T1ID]
      ,[Name]
  FROM [AdventureWorks2012].[Person].[T2]

  insert into [AdventureWorks2012].[Person].[T2] values(NULL,'efwe')

  select sum(T2ID),T1ID from  [AdventureWorks2012].[Person].[T2]
  group by T1ID


  select count(*) from   [AdventureWorks2012].[Person].[T2]
  
  select count(T1ID) from   [AdventureWorks2012].[Person].[T2]


  create table  [AdventureWorks2012].[Person].[Test2]
  (col1 char(1),
  col2 char(1),
  col3 char(1))

  insert into  [AdventureWorks2012].[Person].[Test2] values ('a','b', 'd')
  insert into  [AdventureWorks2012].[Person].[Test2] values ('e',NULL, 'g')
  insert into  [AdventureWorks2012].[Person].[Test2] values ('h','i', 'k')
  insert into  [AdventureWorks2012].[Person].[Test2] values ('l',NULL, 'n')
  insert into  [AdventureWorks2012].[Person].[Test2] values ('o',NULL, 'q')

  select * from [AdventureWorks2012].[Person].[Test1]
  select * from [AdventureWorks2012].[Person].[Test2]
  select * from [AdventureWorks2012].[Person].[Test1] a left outer join [AdventureWorks2012].[Person].[Test2]  b
  on a.col1=b.col1
  and a.col2=b.col2

  select * from [AdventureWorks2012].[Person].[Test1] a inner join [AdventureWorks2012].[Person].[Test2]  b
  on a.col1=b.col1  and (coalesce(a.col2,'')=coalesce(b.col2,''))

  
  (a.col2=b.col2 or a.col2 is null or b.col2 is null)


create table countries
(country_id varchar(2),
country_name varchar(30),
region_id int)


CREATE TABLE IF NOT EXISTS jobs_dups ( 
JOB_ID varchar(10) NOT NULL , 
JOB_TITLE varchar(35) default ' ' , 
MIN_SALARY decimal(6,0) check(min_salary>1000) default 8000, 
MAX_SALARY decimal(6,0) check(max_salary<25000) 
);

create table countries_dup
(
country_id varchar(2) unique,
name varchar(20) check(name in ('India','China')),
region int,
date_entered date check (date_entered like '--/--/----')
);

CREATE TABLE IF NOT EXISTS jobs_dups ( 
JOB_ID varchar(10) NOT NULL , 
JOB_TITLE varchar(35) default ' ' , 
MIN_SALARY decimal(6,0) default 8000 check(min_salary>1000), 
MAX_SALARY decimal(6,0) default NULL
);


update employees
set SALARY =case when department=40 then (salary+.25*salary) when department=90 then (salary+.15*salary) when  department=110 then (salary+.10*salary) else salart end



 select job_id, avg(salary),count(*) from employees
 group by department_id
 having count(*)>10;

 select e1.first_name,e1.last_name from employees e1,
 employees e2,
 departments d,
 locations l
 where e1.manager_id=e2.employee_id
 and e2.department_id=d.department_id 
 and d.location_id= l.location_id
 and l.country_id='US'

 

 select e2.first_name, e2.last_name FROM employees e2
 where employee_id in (select manager_id from employees);

  SELECT e2.first_name, e2.last_name FROM employees e1, 
 employees e2
 where e1.manager_id=e2.employee_id;   

 select e2.first_name, e2.last_name FROM employees e2
 where salary >(select avg(salary) from employees);

 select  e2.first_name, e2.last_name FROM employees e2,
 (select avg(salary) avg_sal from employees)e3
 where e2.salary>e3.avg_sal

select distinct  e2.first_name,e2.last_name from employees e1 left outer join
employees e2 on e1.manager_id=e2.employee_id
where e2.employee_id is not  null

 select e1.first_name,e1.last_name, e1.salary from employees e1, jobs j
 where e1.job_id=j.job_id
 and e1.salary=j.min_salary

 --min 3
   select e1.first_name,e1.last_name, e1.salary from employees e1
   where (select count(distinct(salary)) from employees where salary<e1.salary)<3

   -- max 3 
   select e1.first_name,e1.last_name, e1.salary from employees e1
   where (select count(distinct(salary)) from employees where salary>e1.salary)<3

      select e1.first_name,e1.last_name, e1.salary from employees e1
   where (select count(distinct(salary)) from employees where salary>e1.salary)in (0,1,2)

   -- 3rd highest
select e1.first_name,e1.last_name, e1.salary from employees e1
   where 3=(select count(distinct(salary)) from employees where salary>=e1.salary)

   
select e1.first_name,e1.last_name, e1.salary from employees e1
   where 2=(select count(distinct(salary)) from employees where salary>e1.salary)

select DEPARTMENT_NAME      
from 
departments where not exists (select 1 from employees where DEPARTMENT_ID=departments.DEPARTMENT_ID)


select e1.first_name,e1.last_name, e1.salary
from employees e1,
(select avg(salary) avg_sal,department_id from employees
group by department_id)
e2
where e1.department_id=e2.department_id
and e1.salary>e2.avg_sal

--no manager
select e1.first_name,e1.last_name, e1.salary,e1.employee_id,e1.manager_id
from employees e1
where not exists(select  1 from employees where employee_id=e1.manager_id);

select e1.first_name,e1.last_name, e1.salary
from employees e1
where employee_id not in (select manager_id from employees );


select e1.first_name,e1.last_name, e1.salary
from employees e1
where not exists (select 1 from employees e2 where e2.manager_id=e1.employee_id);


select  e1.first_name,e1.last_name, e1.salary, coalesce(e2.manager_id,'No Manager')
from employees e1 left outer join 
employees e2
on e1.manager_id=e2.employee_id
where e2.employee_id is not null




select  e1.first_name,e1.last_name, e1.salary, coalesce(e2.manager_id,'Not Manager')
from employees e1 left outer join 
employees e2
on e2.manager_id=e1.employee_id
where e2.manager_id is  null



select e1.first_name,e1.last_name, e1.salary emp_sal, e2.salary mgr_sal
from employees e1 left outer join 
employees e2
on e1.manager_id=e2.employee_id
where e1.salary>0.5*e2.salary
and  e2.manager_id is  not null


select  e1.employee_id,e1.first_name,e1.last_name, 
e2.employee_id as managerID, e2.first_name, e2.last_name
from employees e1 left outer join 
employees e2
on e1.manager_id=e2.employee_id
where
  e2.employee_id is not null and  e1.manager_id =100;


 select  e1.employee_id,e1.first_name,e1.last_name, 
e2.employee_id as managerID, e2.first_name, e2.last_name
from employees e1 inner join 
employees e2
on e1.manager_id=e2.employee_id
where
  e2.employee_id is not null and  e1.manager_id =100


select  e1.employee_id,e1.first_name,e1.last_name
from employees e1 
where
  manager_id =100


  select DEPARTMENT_NAME     ,
  first_name, last_name,salary
  from departments d, employees e
  where d.manager_id=e.epmployee_id
  and datediff(,'y',HIRE_DATE , current_date)
