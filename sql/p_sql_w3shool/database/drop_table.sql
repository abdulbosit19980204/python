-- PostgreSQL DROP TABLE
-- The DROP TABLE Statement

-- The DROP TABLE statement is used to drop an existing table in a database.

-- Note: Be careful before dropping a table. Deleting a table will result in loss of all information
-- stored in the table!

-- The following SQL statement drops the existing table cars.

-- Example

-- Delete the cars table:
DROP TABLE cars;

-- RESULT
-- DROP TABLE


-- Display TABLE
-- To check the result we can display the table with this SQL statement.

SELECT *
FROM cars;

-- Which will result in an error, because the cars table no longer exists.
-- Result
-- ERROR: relation "cars" does not exist
-- LINE 1: SELECT * FROM cars;



