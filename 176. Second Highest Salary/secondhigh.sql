SELECT MAX(SALARY) AS SecondHighestSalary  FROM Employee WHERE (SALARY < (SELECT MAX(SALARY) FROM Employee))