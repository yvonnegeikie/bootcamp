-- mySQL day 2 -------------

CREATE DATABASE School;
USE School;
CREATE TABLE Class(
	studentId INT PRIMARY KEY,
    studentName VARCHAR(15) NOT NULL,
    studentClass INT NOT NULL,
    studentMark INT CHECK(studentMark >=0 AND studentMark<=100),
    studentGender ENUM ('male','female')
    );

DESCRIBE Class;
INSERT INTO Class(studentId, studentName, studentClass, studentMark, studentGender) VALUES
(1, 'Sophie', 6, 50, 'female');
INSERT INTO Class(studentId, studentName, studentClass, studentMark, studentGender) VALUES
(2, 'Rosie', 6, 50, 'female');
INSERT INTO Class(studentId, studentName, studentClass, studentMark, studentGender) VALUES
(3, 'Harry', 5, 100, 'male');
INSERT INTO Class(studentId, studentName, studentClass, studentMark, studentGender) VALUES
(4, 'Ben', 4, 43, 'male'),
(5, 'Sam', 2, 55, 'male'),
(6, 'Laura', 4, 99, 'female');
SELECT * FROM Class;

INSERT INTO Student(studentName, studentAge, studentLocation) VALUES ('Bonnie', 20, 'Melbourne');
INSERT INTO Student(studentName, studentAge) VALUES ('Sophie', 20);

-- task -------------- 
CREATE DATABASE World;
USE World;

CREATE TABLE Country(
id INT PRIMARY KEY,
countryName VARCHAR (15) NOT NULL
);
CREATE TABLE City(
cityId INT PRIMARY KEY,
cityName VARCHAR (20) NOT NULL,
countryId INT, 
FOREIGN KEY (Countryid) REFERENCES Country(Id)
);
DESCRIBE City;

-- Update data 
-- UPDATE tableName SET columnName=value WHERE Condition 

USE School;
SELECT * FROM Class;

UPDATE Class SET studentName = 'Angelica' WHERE studentId = 1; -- name changed from Sophie to Angelica
UPDATE Class SET studentName= 'Smith', studentGrade= 23, studentClass= 6 WHERE studentId= 3;
SET SQL_SAFE_UPDATES=0;

-- task 
USE Newwork;
CREATE DATABASE NewWork;
CREATE TABLE Department(
Depotno INT PRIMARY KEY, 
Dname VARCHAR (20) NOT NULL, 
Loc VARCHAR (20) NOT NULL
);
CREATE TABLE Employee(
Empno INT PRIMARY KEY,
Ename VARCHAR (20) NOT NULL, 
Job VARCHAR (20) NOT NULL, 
Depotno INT,
FOREIGN KEY (Depotno) REFERENCES Department(Depotno)
);
SELECT * FROM NewWork;















