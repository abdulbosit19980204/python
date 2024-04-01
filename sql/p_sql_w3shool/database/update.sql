-- PostgreSQL Update

-- The UPDATE Statement
-- The UPDATE statement is used to modify the value(s) in existing records in a table.

-- Example
-- Set the color of the Volvo to 'red'
UPDATE cars
SET color = 'red'
WHERE brand = 'Volvo';

-- Result
-- UPDATE 1

-- Which means that 1 row was affected by the UPDATE statement.

-- Note: Be careful with the WHERE clause, in the example above ALL rows where brand = 'Volvo'  gets updated.

-- Display TABLE
-- To check the result we can display the table with this SQL statement:

SELECT *
FROM cars;


-- Warning! Remember Where

-- Be careful when updating records. If you omit the WHERE clause, ALL records will be updated!
-- Without the Where clause, All records will be updated:

UPDATE cars
SET color ='red';

-- Result
-- UPDATE 4

-- Which means that all 4 row was affected by the UPDATE statement.

-- Display Table
-- To check the result we can display the table with this SQL statement

SELECT *
FROM cars;

-- UPDATE Multiple Columns
-- To update more than one column, separate the name/value pairs with a comma

-- Example
-- Update color and year for the Toyota:

UPDATE cars
SET color = 'white',
    year  =1920
WHERE brand = 'Toyota';


SELECT *
FROM cars;

