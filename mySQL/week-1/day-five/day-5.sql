
-- mySQL day 5

-- AS keyword 
-- renames 
-- IN keyword 
-- nested queries 
-- display all employeed whos name is 'john', 'jennifer', 'ahmad' or 'alice 
SELECT* FROM Employee WHERE FNAME IN ('john', 'jennifer', 'ahmad', 'alice');

-- DISTINCT keyword 
-- selects unique data 
SELECT salary FROM Employee; -- shows all salarys, some multiple times 
SELECT DISTINCT salary FROM Employee; -- shows all salary amounts only once 

-- Aggregate functions 
-- AVG(), MAX(), MIN(), SUM(), COUNT() 

-- what is average salary in company? 
SELECT AVG (salary) AS 'average salary' FROM Employee; 

-- what is the total amount of salary you pay to all employees?
SELECT SUM(salary) AS 'total salary' FROM employee; 

-- How many employees ar eworking in your company?
SELECT COUNT(*) 'total number of employees' FROM Employee; -- = 9
SELECT COUNT(salary) 'total number of employees' FROM Employee; -- does not show those with NUL salary 
SELECT * FROM Employee; -- shows all including NUL for salary 

-- display max and min salary that you pay to your employees 
select max(salary) as 'max salary', min(salary) as 'min salary' from employee;

-- display max and min salary for male employees 
select max(salary) as 'max salary', min(salary) as 'min salary' from employee where sex='m';

-- Grouping data 
-- Group BY
-- groups rows that have the same values into summary rows 
-- Display ho many male and how many female employees are working in the company 
SELECT sex, COUNT(*) AS 'no of emp' FROM employee WHERE sex IS NOT NULL GROUP BY sex; 

-- display highest salary for each gender
SELECT sex, MAX(salary) AS 'max salary' FROM Employee WHERE sex IS NOT NULL GROUP BY sex; -- group baed on sex column 

SELECT address, COUNT(*) FROM employee GROUP BY address; 
SELECT * FROM employee; 

-- % LIKE 
SELECT * FROM employee WHERE fname LIKE 'j%'; -- names startin with J
SELECT * FROM employee WHERE fname LIKE '%n'; -- names ending in N
SELECT * FROM employee WHERE fname LIKE '_o%'; -- names that have o in the second position 
SELECT * FROM employee WHERE fname LIKE '_o'; -- name  should be only 2 characters and o should be 2nd character 
SELECT * FROM Employee WHERE fname LIKE 'j____%'; -- name should start with J and be minimun 5 charater in length 

-- TASK 
-- select all employees who name has 'h' as second character
SELECT * FROM employee WHERE fname LIKE '_h%';

-- SELECT Employees who has 'me' in their first name.
SELECT * FROM employee WHERE fname LIKE '%me%';

-- Select employees who's first Name can be anything but should have 'oh' after first character.
SELECT * FROM employee WHERE fname LIKE '%_oh%';
-- Select record of Employee who is born in 1965.
SELECT * FROM employee WHERE bdate LIKE '1965-__-__';
SELECT * FROM employee WHERE bdate LIKE '1965-%';
SELECT * FROM employee WHERE YEAR (bdate) =1965;

-- Display all employees who's first Name starts with A and ends with d.
SELECT * FROM employee WHERE fname LIKE 'a%' AND lname LIKE '%d';
SELECT * FROM employee WHERE fname LIKE 'a%n';

-- Display all employees who's first Name start with J and does not ends with n.
SELECT * FROM employee WHERE fname LIKE 'j%' AND fname NOT LIKE '%n';

-- next week UNION and JOIN 









