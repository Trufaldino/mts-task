-- A

SELECT e1.name
FROM employee e1
INNER JOIN employee e2 ON e1.chief_id = e2.id
WHERE e1.salary > e2.salary;


-- B
SELECT e1.name
FROM employee e1
WHERE e1.salary = (
    SELECT MAX(salary)
    FROM employee e2
    WHERE e1.department_id = e2.department_id
);


-- C
SELECT department_id
FROM employee
GROUP BY department_id
HAVING COUNT(*) <= 3;

-- D
SELECT e1.name
FROM employee e1
LEFT JOIN employee e2 ON e1.id = e2.chief_id
WHERE e2.id IS NULL AND e1.department_id = e2.department_id;

-- E
SELECT department_id
FROM (
    SELECT department_id, SUM(salary) AS total_salary
    FROM employee
    GROUP BY department_id
) AS department_salary
WHERE total_salary = (
    SELECT MAX(total_salary)
    FROM (
        SELECT department_id, SUM(salary) AS total_salary
        FROM employee
        GROUP BY department_id
    ) AS max_salary
);
