-- mySQL week2, DAY 8 
-- task 

-- Write a query that return the current logged-in user name -- 
SELECT USER(); -- root@localhost
SELECT CURRENT_USER(); -- root@localhost

-- Write a query which displays current month name -- 
SELECT MONTHNAME(CURDATE()); -- February
SELECT DATE_FORMAT(CURRENT_DATE(), '%M');  -- February

-- Write a query which returns today name -- 
SELECT DAYNAME(CURDATE()); -- Wednesday

-- Write a query that returns the current date -- 
SELECT CURDATE(); -- 2024-02-14

-- Write a query that returns current time -- 
SELECT TIME(NOW()); -- 09:20:57
SELECT CURRENT_TIMESTAMP(); -- 2024-02-14 09:24:08

-- Write a query that return the current year -- 
SELECT YEAR(CURDATE()); -- 2024

-- Write a query which returns current date and time -- 
SELECT NOW(); -- 2024-02-14 09:22:08

-- Write a query that retruns employee FNAME in upper case --
SELECT UCASE(FNAME) FROM employee; 


CREATE DATABASE World;

USE World;
CREATE TABLE Country
(
	id INT PRIMARY KEY,
    name VARCHAR(20) NOT NULL
);

CREATE TABLE City
(
	cityId INT PRIMARY KEY,
    cityName VARCHAR(15) NOT NULL,
    countryId INT
);

ALTER TABLE City ADD FOREIGN KEY(countryId) REFERENCES Country(id) ON DELETE SET NULL;
INSERT INTO Country (id, name) VALUES (1,'UK'),(2,'USA'),(3,'Germany');
INSERT INTO City VALUES (1, 'London',1),(2,'Manchester',1),(3,'New York',2),(4,'Berlin',3);

SELECT * FROM Country;
SELECT * FROM City;
DELETE FROM Country WHERE name='UK';

/* Create these two tables, when you delete a department, in the employee table it's 
DepNo value should be set to Null for any employee who is working in that specific department! */

create table employee(
EmpNo int primary key, 
EmpName varchar (10),
DeptNo int
);

create table department(
DepNo int primary key,
DName varchar (20),
Location varchar (30)
);

alter table employee add foreign key (DepNo) references department (DepNo) on delete set null;

-- ROLLBACK
-- will apply to the last data that was deleted, only applied to data, not tables or database etc 
set autocommit =0;
select * from country; 
select *from city;
delete from country where name = 'Germany';

ROLLBACK; -- will bring back last move EXCEPT if TRUNCATE used 
COMMIT; -- once coommited there is not abiblity to rollback 


