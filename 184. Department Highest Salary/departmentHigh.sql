SELECT D.name as Department, E.name as Employee, E.salary as Salary FROM Employee E
INNER JOIN Department D ON D.id = E.departmentId
WHERE (E.departmentId, E.salary) IN (select departmentId, max(salary) from Employee Group by departmentId)
GROUP BY D.name, E.name