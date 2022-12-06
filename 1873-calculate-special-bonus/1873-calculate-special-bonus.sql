# Write your MySQL query statement below
select employee_id, salary as bonus
from Employees
where employee_id%2!=0 and name not like 'M%'

union

select employee_id, 0
from Employees
where (employee_id%2!=0 and name like 'M%') or
      (employee_id%2=0 and name not like 'M%') or
      (employee_id%2=0 and name like 'M%')
order by employee_id
