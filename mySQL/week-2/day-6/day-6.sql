-- mySQL, week 2, day 6 
-- JOIN 
-- INNER JOIN, LEFT JOIN, RIGHT JOIN, CROSS JOIN 

USE company; 

-- display all employee and their deptartment name 
SELECT fname, lname, dname FROM employee INNER JOIN department ON DNO=DNUMBER;
SELECT * FROM department;
SELECT * FROM dept_locations;
SELECT dname, dlocation FROM department d INNER JOIN dept_locations dl ON 
d.dnumber=dl.dnumber; 

CREATE database Monday;
USE Monday;

CREATE table employee(
EmpNo int,
EmpName VARCHAR (30),
DeptNo int
);

CREATE TABLE department(
DeptNo int,
DName varchar (30),
Location varchar (30),
primary key (DeptNo)
);

ALTER TABLE employee ADD FOREIGN KEY (DeptNo) REFERENCES department(deptNo);
ALTER TABLE employee ADD PRIMARY KEY (EmpNo);

INSERT INTO department VALUES (1, 'HR', 'London'), (2, 'software', 'London'), (3, 'IT', 'manchester');
INSERT INTO employee VALUES(1, 'Beautriz', 1),(2, 'Zak', 2),(3, 'Matt', 2),(4, 'Waqas', 2),(5, 'Mark', 2),(6, 'john', NULL);

-- display employees and thier department name 
SELECT EmpName, Dname FROM employee INNER JOIN department ON employee.DepNo=department.deptNo;
-- display all employees and their department 
SELECT EmpName, Dname FROM employee LEFT JOIN department ON department.deptNo=employee.deptNo;

CREATE TABLE instructor(
InstructorID int, 
InstructorName varchar (30),
primary key (InstructorID)
);

CREATE TABLE trainer(
TrainerID int, 
TrainerName varchar (30),
TrainerAge int,
primary key (TrainerID)
);

INSERT INTO instructor VALUES (2, 'mark'), (1, 'Abdul'), (3, 'matt'), (4, 'Sandara');
INSERT INTO trainer VALUES (1, 'abdul', 32), (2, 'Zak', 26), (3, 'Waqas', 36);

SELECT * FROM trainer INNER JOIN instructor ON instructorName = trainerName; 
SELECT * FROM trainer LEFT JOIN instructor ON instructorName = trainerName; 
SELECT * FROM trainer RIGHT JOIN instructor ON instructorName = trainerName; 

-- link miltuple tables 
USE company;
-- display employee name, the project name which they work and the hours per week they work 
SELECT fname, lname, pname, hours FROM employee LEFT JOIN
Works_On ON ESSN=SSN
INNER JOIN project ON PNO=Pnumber;

-- display department name and their manager name
SELECT fname, lname, Dname FROM employee
INNER JOIN department ON mgrssn=ssn;