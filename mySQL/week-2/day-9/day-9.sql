-- mySQL week 2, day 9 
-- case expression 
-- deimiter
-- trigger 

USE company;
select fname, lname, 
case 
when salary=25000 then salary+2500
end as 'new salary'
from employee;
select * from employee;

select fname, lname,
 case 
   when sex='f' then 'female'
   when sex='m' then 'male'
  end as 'gender' 
from employee;    

-- CASE -- TASK 
-- Write a case expression that returns employee's full name salary with bonus as below:
-- if salary is 1000 - 19000 increase 1000 
-- if salary is 20000 - 29000 increase 2000
-- if salary is 30000 - 39000 increase 3000
-- if salary is 40000 - 49000 increase 4000
-- if salary is 50000 - 59000 increase 5000
-- if a person receive no salary then should display 'Not eligible for bonus'

    SELECT CONCAT(fname, ' ',lname) AS 'employee name', salary,
     case 
      when salary between 1000 and 19000 then salary +1000
      when salary between 20000 and 29000 then salary +2000
      when salary between 30000 and 39000 then salary +3000
      when salary between 40000 and 49000 then salary +4000
	  when salary between 50000 and 59000 then salary +5000
      -- when salary is null then 'not eligible for bonus' -- this works as well 
      else 'not eligible for bonus'
     end as 'New salary'
    FROM employee; 
    
/*
I would like you to increase the salary of employees based on their departments
    for example, if an employee is working in the Research department increase it's salary
    by 5000 and for other departments as well any amount you want.
*/

select concat(fname, ' ', lname) as 'employee', dname, salary,
  case 
    when dname = 'research' then salary + 5000
    when dname = 'administration' then salary + 4000
	when dname = 'headquarter' then salary + 3000
    else 'Sorry you not eligible'
  end as 'salary with bonus' 
  from employee left join department on dno=dnumber; 
    
create table LogInfo(
message text not null
);

-- delimiter 
-- trigger 

DELIMITER $$
CREATE TRIGGER deleteData AFTER DELETE ON Employee FOR EACH ROW
	BEGIN
		INSERT INTO LogInfo (Message) VALUES(CONCAT(OLD.name,' was deleted by ',
        CURRENT_USER(),' on ',CURDATE(),' and ', CURTIME()));
    END$$

    DELIMITER $$
CREATE TRIGGER updateData AFTER UPDATE ON Employee FOR EACH ROW
	BEGIN
    INSERT INTO LogInfo (Message) VALUES(CONCAT(OLD.name,' name was change to ',NEW.name, ' by ', CURRENT_USER()));
END$$

-- Stored proceedure 
-- Case expression 
-- Increase code reuabiltuy and reduce netwoek traffic 

Change delimiter
CREATE PROCEUDRE procedureName(optional parameter)
  BEGIN
  
  END NewDelimiter

USE company; 

delimiter *** 
create procedure allEmployee()
  begin 
    select * from employee;
  end***
  
  call allEmployee(); 
  drop procedure allEmployee;
	
-- will have a parameter and first name 
-- parameters used in stored procedures = IN, OUT, INOUT 

delimiter @@
create procedure employee(in firstName varchar (20))
  begin 
  select * from employee where Fname=firstName; 
  end@@

 call Employee("john"); 
 call allEmployee(); 
 
/*
-- TASK 
- Write procedure which deletes employee whose name you're passing as an argument --
- Create a procedure which will display an employee record whose 
  first and last anme you're passong as an argument --
  */

delimiter @@
create procedure employee (IN delete_name varchar (20))
begin 
delete from employee where concat(fname, ' ,', lname) = delete_name;
end@@

select * from uniondb.employee;
delimiter $$
create procedure deleteEmployee(in employeeName varchar (20))
begin 
delete from employee where name=employeeName;
select * from employee;
end$$ 
call deleteEmployee("Pratish"); 

delimiter£££
create procedure anEmployee(in varchar (20), in varchar(20))
begin
select * from employee where Fname-fn and Lname=ln; 
end£££ 
call anEmployee('John', 'Smith');

	
