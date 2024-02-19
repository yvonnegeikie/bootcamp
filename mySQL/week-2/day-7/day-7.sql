-- mySQL WEEK 2, DAY 7 

-- CROSS JOIN raely used 
-- if we use conditions then result will be same a using inner join 
-- INNER, LEFT, RIGHT used frequently

-- show employee name and their manager name 
SELECT CONCAT (e.fname, ' ',e.lname) AS 'Employee', 
CONCAT(m.fname, ' ', m.lname) AS 'Manager' FROM Employee AS e LEFT JOIN Employee AS m
ON e.SuperSsn=m.Ssn;

SELECT CONCAT (e.fname, ' ',e.lname) AS 'Employee', e.Ssn, e.BDATE, e.Address, e.Sex, e.SuperSsn,
CONCAT(m.fname, ' ', m.lname) AS 'Manager' FROM Employee AS e LEFT JOIN Employee AS m
ON e.SuperSsn=m.Ssn;

SELECT CONCAT(fname, ' ', lname) AS 'Full Name', CONCAT('£  ', salary, 'Per Year') AS 'Salary' 
FROM Employee; 

SELECT CONCAT(fname, ' ', lname) AS 'Full Name', CONCAT('£  ', salary+1000, ' Including bonus') AS 'Salary' 
FROM Employee; 
-- String function 
-- Date functions 

SELECT TRIM('                  Yvonne            ') AS NAME; -- removed space around string 
SELECT RTRIM('                  Yvonne            ') AS NAME; -- space remains to the left 
SELECT UCASE (fname) AS 'First Name', LCASE (lname) AS 'Last Name' FROM employee; -- change case 

-- display full name of employees in uppercase 
SELECT UCASE (CONCAT(fname, ' ', lname)) AS 'Employee Name' FROM employee; 

-- ***** CONCAT is a *FUNCTION* so *MUST* be enclosed in parenthes same as SUM, etc 

-- SUBSTRING selects content fro mithin a string to use starting with charhact and ending with character 
SELECT SUBSTRING('Database', 1, 4); -- Data is displayed 
SELECT SUBSTRING('Database', 5, 8); -- base is displayed 
SELECT SUBSTRING('Database', 1); -- database is displayed 

/*
NOW()/CURRENT_TIMESTAMP()
CURDATE()/CURRENT_DATE()
CURTIME()/CURRENT_TIME()
MONTHNAME()   DAYNAME()
DAY()
YEAR()
*/ 

SELECT NOW(); -- 2024-02-13 11:38:47
SELECT CURDATE(); -- 2024-02-13
SELECT CURTIME(); -- 11:39:08
SELECT MONTHNAME(CURDATE()); -- February
SELECT MONTHNAME('2024-02-13'); -- February
SELECT DAYNAME('1989-09-16'); -- Saturday

SELECT * FROM Employee WHERE YEAR(BDATE)>1960;

-- TASK
-- display Tuesday, 13 February 2024
SELECT concat(dayname(curdate()),' ,',date_format(curdate(),'%W %e %M %Y')) AS 'Current date';
-- Corne 
SELECT DATE_FORMAT(CURDATE(), '%W, %e, %M, %Y') AS 'Current date';
-- Zak 
SELECT CONCAT(DAYNAME(CURDATE())), ', ', DAY(CURDATE()), ', ',
MONTHNAME(CURDATE()), ', ', YEAR(CURDATE());
-- Begard 
SELECT concat(dayname(curdate()),',',date_format(curdate(),'%e %M %Y')) as 'Current date';

DELETE FROM employee WHERE fname ='Jennifer'; -- doest work 

-- tomorrow 
-- ON DELETE CASCADE 
-- ON DELETE SET NULL 
-- ROLLBACK 