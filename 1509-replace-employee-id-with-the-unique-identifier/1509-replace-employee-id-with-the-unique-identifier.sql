/* Write your T-SQL query statement below */
select empU.unique_id, emp.name from employees emp
left join employeeUNI empU on emp.id=empU.id