-- PostgreSQL ADD COLUMN

-- The ALTER TABLE Statement
-- To add a column to an existing table, we have to use the ALTER TABLE statement.
-- The "ALTER TABLE" statement is used to add, delete, or modify columns in an existing table
-- The "ALTER TABLE" statement is also used to add and drop various constraints on an existing table

-- ADD COLUMN
-- We want to add a column named color to our cars table.
-- When adding columns we must also specify the data type of the column. Our color column will be a string,
-- and we specify string types with the VARCHAR keyword. We also want to restrict the number of characters to 255.

-- Example
-- Add a column named color:
ALTER TABLE cars
    ADD color VARCHAR(255);

-- Result
-- ALTER TABLE

-- Display TABLE
-- To check the result we can display the table with this SQL statement:

SELECT *
FROM cars;

-- As you can see, the cars table now has a color column.
-- The new column is empty, you will learn how to fill it with values in the next chapter.

