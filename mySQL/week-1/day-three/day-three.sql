
-- mySQL day 3

-- create a complex schema 
-- first create all tables with primary key 
-- once all tables created, then add forign key using altre comand

-- task 2
-- recreate schema as seen in jpg.

create database planet; 
use planet;

create table country(
code int primary key, 
name varchar (50),
continent varchar (30),
population int,
capital int
);

create table city(
id int primary key,
name varchar (20) not null,
countryCode int,
population int
);

create table countryLanguage(
countryCode int,
language varchar (30), 
isOfficial boolean, 
percentage decimal (4,1),
primary key(countryCode, language)
);

alter table country
add foreign key(capital)
  references city (id);
  
alter table city 
add foreign key (countryCode) 
  references country(code); 
  
alter table countryLanguage
add foreign key (countryCode)
  references country(code);
  
  -- task 3
  -- create schema as seen in jpg. 
  create database learning;
  use learning;
  
  create table article (
  id int,
  title varchar (30),
  text varchar (30),
  publishStatus boolean, 
  topic varchar (30),
  author varchar(20),
  publicationDate int,
  primary key (id)
  );
  
  create table topic (
  name varchar (30),
  description varchar (50),
  primary key (name)
  );
  
  create table author (
  userName varchar (50),
  displayName varchar (30),
  primary key (username)
  );
  
  create table course (
  shortName int,
  fullName varchar (20),
  primary key (shortName)
  );
  
  create table relevant_for (
  articleID int,
  course int,
  primary key (articleID)
  );
  
  alter table article
  add foreign key (id) references relevant_for (articleID);
  
  alter table article
  add foreign key (topic) references topic (name);
  
  alter table article
  add foreign key (author) references author (userName);
  
  alter table topic 
  add foreign key (name) references article (topic);
  
  alter table author
  add foreign key (username) references article (author);
  
  alter table course
  add foreign key (shortName) references relevant_for (course); 
  
  alter table relevant_for
  add foreign key (articleID) references ID (article);
  
  alter table relevant_for
  add foreign key (course) references article (ID);
  
  













