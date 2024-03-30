-- PostgreSQL Insert Data

-- Insert Into

-- To insert data into a table in PostgreSQL, we use the "INSERT INTO" Statement.
-- The following SQL statement will insert one row of data into the cars table you created in the previous chapter

INSERT INTO cars(brand, model, year)
VALUES ('Ford', 'Mustang', 1964);

-- The SQL Shell application will return the following
-- INSERT 0 1

-- Which means that 1 row was inserted


-- SQL Statement Explained
-- As you can see in the SQL statement above, string values must be written with apostrophes.
-- Numeric values can be written without appostrophes, but you can include them if you want

-- Display Table
-- To check the result we can display the table with this SQL statement:

SELECT *
FROM cars;

-- Which will return this result:

brand |  model  | year
-------+---------+------
 Ford  | Mustang | 1964
(1 row)

-- Insert multiple Rows

-- To insert multiple rows of data, we use the same INSERT INTO statement, but with multiple values:
INSERT INTO cars(brand, model, year)
VALUES ('Volvo', 'p1800', 1968),
       ('BMW', 'M1', 1978),
       ('Toyota', 'Celica', 1975);

-- The SQL SHell application will return the following:
-- INSERT 0 3

-- Which means 3 rows were successfully inserted.

-- Display Table
SELECT *
FROM cars
