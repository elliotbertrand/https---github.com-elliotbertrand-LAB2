DROP DATABASE IF EXISTS lab2_elliot;
CREATE DATABASE lab2_elliot;

USE lab2_elliot;

DROP TABLE IF EXISTS weather_data;
CREATE TABLE weather_data (
   Month_ID int NOT NULL PRIMARY KEY,
   Month varchar(255) NOT NULL,
   Avg_Max_Temp float,
   Avg_Min_Temp float,
   Mean_Temp float,
   Highest_Temp float,
   Lowest_Temp float,
   Total_Rain float,
   Most_Rain float,
   Raindays int,
   Total_Sun float,
   Most_Sun float,
   Max_Wind float
);

INSERT INTO weather_data (Month_ID, Month)
VALUES ('1', 'December 2022');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('2', 'November 2022');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('3', 'October 2022');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('4', 'September 2022');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('5', 'August 2022');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('6', 'July 2022');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('7', 'June 2022');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('8', 'May 2022');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('9', 'April 2022');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('10', 'March 2022');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('11', 'February 2022');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('12', 'January 2022');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('13', 'December 2021');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('14', 'November 2021');

INSERT INTO weather_data (Month_ID, Month)
VALUES ('15', 'October 2021');
