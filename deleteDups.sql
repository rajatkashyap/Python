

select * from employees e1 left outer join 
(select max(id) id,department_id
from employees
group by department_id)e2
on e1.id=e2.id
where e2.id is null 


with recursive cte as
(
  select department_id, row_number() over(partition by department_id order by department_id) rn
  from employees
  )
  select * from cte where rn<>1 ; */
  
delete  e1 
from employees e1, employees e2
where e1.department_id=e2.department_id
and e1.id>e2.id; 


/*delete e1 from employees e1 left outer join  
employees e2
on e1.department_id=e2.department_id where e1.id>e2.id */


DELETE FROM TableName
WHERE  ID NOT IN (SELECT MAX(ID)
                  FROM   TableName
                  GROUP  BY Column1,
                            Column2,
                            Column3
                  /*Even if ID is not null-able SQL Server treats MAX(ID) as potentially
                    nullable. Because of semantics of NOT IN (NULL) including the clause
                    below can simplify the plan*/
                  HAVING MAX(ID) IS NOT NULL) 
				  
				  
select  distinct * into t2 from t1;
delete from t1;
insert into t1 select *  from t2;
drop table t2;


  delete e1
  from [AdventureWorks2012].[HumanResources].[emp] e1,
  [AdventureWorks2012].[HumanResources].[emp] e2
  where e1.name=e2.name
  and e1.mgr_id=e2.mgr_id
  and e1.emp_id>e2.emp_id


delete from  [AdventureWorks2012].[HumanResources].[emp] 
where emp_id not in (select 
