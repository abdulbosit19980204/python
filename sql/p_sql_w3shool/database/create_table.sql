-- PostgreSQL Create Table

-- Connect to the Database
-- To create a new database table using the SQL Shell, make sure you are connected to the database.
-- If not, follow the steps in the GET Started chapter of this tutorial.
-- Once you are connected, you are ready to write SQL Statement


-- CREATE TABLE
-- The following SQL statement will create a table named cars in your PostgreSQL database:

CREATE TABLE cars
(
    brand VARCHAR(255),
    model VARCHAR(255),
    year  INT
);

-- When you execute the above statement, an empty table named cars will be created,
-- and the SQL Shell application will return the following  CREATE TABLE

-- SQL Statement Explained
-- The above SQL statement created an empty table with three fields: brand, model, and year
-- When creating fields in a table we have to specify the data type of each field
-- For brand and model we are excepting string values, and string values are specified with the VARCHAR keyword
-- We also have to specify the number of characters allowed in a string field, and since we don't know exactly,
-- we just set it 255.

-- For year we are expecting  integer values (numbers without decimals),
-- and integer values are specified with the INT keyword.


-- Display TABLE

-- You can "display" the empty table you just created with another SQL statement
SELECT * FROM cars;

-- Which will give you result
 brand | model | year
-------+-------+------
(0 rows)



