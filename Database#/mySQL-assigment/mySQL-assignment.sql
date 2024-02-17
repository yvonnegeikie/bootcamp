-- ----- assisgnmnt -------------------------------------------------------------------------
-- -------------------task 1--------------------------------------------------------------------
create database breakdownCompany;
use breakdownCompany;

create table Members(
MemberID int(10),
MemberFName varchar(20), 
MemberLName varchar(20), 
MemberLoc varchar(20),
primary key (MemberID)
);

create table Vehicle(
VehicleReg varchar(10),
VehicleMake varchar(10),
VehicleModel varchar(10),
MemberID varchar(10),
primary key (VehicleReg)
);

alter table Vehicle modify column MemberID int;

create table Engineer(
EngineerID int, 
EngineerFName varchar(20),
EngineerLName varchar(20),
primary key (EngineerID)
);

create table Breakdown (
BreakdownID int (10),
VehicleReg varchar (10),
EngineerID int,
BreakdownDATE date,
BreakdownTIME time,
BreakdownLoc varchar (20),
primary key (BreakdownID)
);

-- ----------------- task 2 -------------------------------
alter table Vehicle add foreign key (MemberID) references Members(MemberID);
alter table Breakdown add foreign key (VehicleReg) references Vehicle (VehicleReg); 
alter table Breakdown add foreign key (EngineerID) references Engineer (EngineerID);

insert into Members (MemberID, MemberFName, MemberLName, MemberLoc)values 
(2020202020,'Lucy', 'Shaw', 'London');

-- MemberID same as in Vehicle top 4 
insert into Members (MemberID, MemberFName, MemberLName, MemberLoc) values 
(303030303,'River', 'Banks', 'Manchester'),
(404040404,'Loona', 'Sky', 'Brighton'),
(505050505,'Earth', 'Potts', 'Bristol'),
(606060606,'Hacking', 'Cough', 'Leeds');
select * from members; 

-- MemberID same as in Member table repeated 
insert into Vehicle (VehicleReg, VehicleMake, VehicleModel, MemberID) values 
('SUN01BURN', 'Mazda', 'M1', 303030303),
('SUN01BURM', 'Honda', 'H2', 404040404),
('SUN01BURZ', 'Suzuki', 'S3', 505050505),
('SUN01BURB', 'Nissan', 'N4', 606060606),
('SUN01BURT', 'Toyota', 'T5', 303030303),
('SUN01BURP', 'Mitsubishi', 'M6', 404040404),
('SUN01BURD', 'Suzuki', 'S7', 505050505),
('SUN01BURG', 'Nissan', 'N8', 505050505);
select * from Vehicle; 

-- EngineerID same as in Breakdown and repeated 
insert into Engineer (EngineerID, EngineerFName, EngineerLName) values
(2234567, 'Blaire', 'Hornne'), 
(4562783, 'Ali', 'Sharpe'), 
(9846327, 'Tyra', 'Flatts');
select * from Engineer; 

-- EngineerID same as in Engineer repeated 3 times 
-- VehicleReg same as in Vehicle repated enough times 
insert into Breakdown (BreakdownID, VehicleReg, EngineerID, BreakdownDATE, BreakdownTIME, BreakdownLoc) 
values 
(123, 'SUN01BURN', '2234567', '2024-01-01', '09:10:57', 'London'),
(124, 'SUN01BURM', '4562783', '2024-01-01', '09:20:57', 'Manchester'),
(125, 'SUN01BURZ', '9846327', '2024-02-01', '09:30:57', 'Leeds'),
(126, 'SUN01BURB', '2234567', '2024-02-02', '09:40:57', 'Leeds'),
(127, 'SUN01BURB', '4562783', '2024-02-03', '09:50:57', 'Brighton'),
(128, 'SUN01BURT', '9846327', '2024-01-13', '08:20:57', 'Bristol'),
(129, 'SUN01BURP', '2234567', '2024-01-14', '07:20:57', 'London'),
(130, 'SUN01BURD', '4562783', '2024-01-15', '06:20:57', 'Leeds'),
(131, 'SUN01BURG', '9846327', '2024-01-16', '05:20:57', 'Manchester'),
(132, 'SUN01BURB', '4562783', '2024-01-17', '04:20:57', 'Bristol'),
(133, 'SUN01BURB', '9846327', '2024-01-18', '03:20:57', 'London'),
(134, 'SUN01BURB', '9846327', '2024-01-19', '02:20:57', 'Manchester');
select * from Breakdown; 

-- ------------------------ TASK 3 -------------------------------------------------------------------
-- The names of members who live in a location e.g. For example, London.
select MemberFName, MemberLName, MemberLoc from members where MemberLoc = 'London';
-- All cars registered with the company e.g. all Nissan cars.
select * from Vehicle where VehicleMake = 'Nissan';

-- The number of engineers that work for the company. 
select COUNT(*) as 'No of company engineers'
from Engineer; 

-- The number of members registered.
select count(*) as 'Number of Members'
from Members; 

-- All the breakdown after a particular date
select * from Breakdown where BreakdownDATE >= '2024-02-01';

-- All the breakdown between 2 dates
select BreakdownDATE from breakdown where BreakdownDATE between '2024-01-15' and '2024-01-19';

-- The number of time a particular vehicle has broken down
select VehicleReg, count(*) as BreakdownCount
from Breakdown
group by VehicleReg;

-- The number of vehicles broken down more than once
SELECT COUNT(DISTINCT VehicleReg) AS "Number of Vehicles Broken Down More Than Once"
FROM Breakdown
WHERE BreakdownID >1;

-- -------------------- TASK 4 -------------------------------------------------------------
-- All the vehicles a member owns. For example, Hacking 
select VehicleReg, VehicleMake, VehicleModel 
from Vehicle
where MemberID = (select MemberID from Members where MemberFName = 'Hacking' and MemberLName = 'Cough');

-- The number of vehicles each member has 
-- sort the data based on the number of car from highest to lowest.
select m.MemberFName, m.MemberLName, count(*) as NumberOfVehicles
from Members m
left join Vehicle v on m.MemberID = v.MemberID
group by m.MemberID, m.MemberFName, m.MemberLName
order by NumberOfVehicles desc;

-- All vehicles that have broken down in a particular location including member details
select b.BreakdownID, v.VehicleReg, v.VehicleMake, v.VehicleModel, m.MemberFName, m.MemberLName, b.BreakdownLoc, b.BreakdownDATE, b.BreakdownTIME
from Breakdown b
inner join Vehicle v on b.VehicleReg = v.VehicleReg
inner join Members m on v.MemberID = m.MemberID
where b.BreakdownLoc = 'Leeds';

-- A list of all breakdown along with member and engineer details between two dates.
select 
    b.*,
    m.MemberFName,
    m.MemberLName,
    e.EngineerFName,
    e.EngineerLName
from Breakdown b
inner join Vehicle v on b.VehicleReg = v.VehicleReg
inner join Members m on v.MemberID = m.MemberID
inner join Engineer e on b.EngineerID = e.EngineerID
where b.BreakdownDATE between '2024-01-15' and '2024-01-19';

-- ----------------------TASK 5 ---------------------------------------------------------
/*A further 3 relational queries of your choice that are meaningful to the company 
using exaples and explaination of functions AVG, MAX, MIN, SUM */

-- the avarage number of cars each member owns rounded down to a whole number.
select MemberFName, MemberLName, round(avg(VehicleCount), 0) as 'Average number of cars'
from (
    select M.MemberID, M.MemberFName, M.MemberLName, COUNT(*) as VehicleCount
    from Members M
    left join Vehicle V on V.MemberID = M.MemberID
    group by M.MemberID, M.MemberFName, M.MemberLName
) as Subquery
group by MemberFName, MemberLName;
-- calculate number of vehicles own per member
-- use LEFT JOIN between Member and Vehicle, including memebr who dont own a car =0
-- avaerage nyumber of vehicles is rounded downt to a whole number for ease of viewing 

-- the sum of all members who live in london
select MemberFName, MemberLName, sum(1) as 'Members who live in London'
from Members
where MemberLoc = 'London'
group by MemberFName, MemberLName;
-- sum is used to count memers who's location is listed as London 

-- the vehicle make with max characters  
select VehicleMake
from Vehicle
where length(VehicleMake) = (select max(length(VehicleMake)) from Vehicle);
-- max and length is used to determin length of characters in VehicleMake 

-- display member location nam with shortest and longests names 
select MemberLoc, min(length(MemberLoc)) as 'shortest loc name', max(length(MemberLoc)) as 'Longest loc name'
from Members
group by MemberLoc
order by MemberLoc;

-- ----------------------TASK 6 --------------------------------------------------------------
/*Create a stored procedure which will display number of cars for any member whoses'
 first name and last name you are passing as argument with calling the stored procedure!*/
DELIMITER //
create procedure GetMemberCarCount(
  in member_fname varchar(20),
  in member_lname varchar(20)
)
begin
  declare total_cars in default 0;
  select count(*) as total_cars
  from Members as m
  inner join Vehicle as v on m.MemberID = v.MemberID
  where m.MemberFName = member_fname and m.MemberLName = member_lname;
  select total_cars;
end //
DELIMITER ;
