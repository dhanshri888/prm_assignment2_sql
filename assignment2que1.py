#Q) Write a SQL statement to create a table named countries including columns country_id, country_name and region_id and 
#make sure that no countries except Italy, India and China will be entered in the table.

# Create a database named assignment
create database assignment;

# Create a table named countries inside assignment database
use assignment;
create table countries(country_id varchar(2) , country_name varchar(40) , region_id decimal(10,0));

# insert values inside countries table
insert into countries values("01" , "Italy" , 1001) , ("02" , "India" , 1002) , ("03" , "China" , 1003);

