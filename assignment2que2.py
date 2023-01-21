2- Write a SQL statement to create the duplicate of the countries table named country_new with all structure and data.

ANSWER

CREATE TABLE country_new ( COUNTRY_ID varchar(2),COUNTRY_NAME varchar(40)CHECK(COUNTRY_NAME IN('Italy','India','China')) ,REGION_ID decimal(10,0));DESC countries;

