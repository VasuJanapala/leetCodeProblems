WITH top_three AS (
    SELECT 
        t1.name as Employee,
        t1.salary as Salary,
        t2.name as Department,
        DENSE_RANK() OVER (PARTITION BY t2.name ORDER BY t1.salary DESC) AS rank_col 
        FROM Employee as t1 JOIN Department as t2 ON t1.departmentId = t2.id
)
SELECT Department, Employee, Salary FROM top_three WHERE rank_col <=3;