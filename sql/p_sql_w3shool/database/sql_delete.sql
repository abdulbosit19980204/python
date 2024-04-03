-- PostgreSQL DELETE

-- The DELETE Statement

-- The Delete statement is used to delete existing records in a table.

-- Note: Be careful when deleting  records in a table! Notice the WHERE clause in the DELETE statement.
-- The WHERE clause specifies which record(s) should be deleted.

-- If you omit the WHERE clause, all records in the table will be deleted!.

-- To delete the records where brand is Volvo, use this statement.

-- Example
-- Delete  all records where brand is 'Volvo'

DELETE
FROM cars
WHERE brand = 'Volvo';

-- RESULT
-- DELETE 1

-- Which means that 1 row was deleted

-- Display table
-- To check the result we can display the table with this SQL statement.
SELECT *
FROM cars;


-- DELETE ALL RECORDS

-- It is possible to delete all rows in a table without deleting the table. This means that the table structure,
-- attributes, and indexes will be intact.
-- The following SQL statement deletes all rows in the cars table, without deleting the table.

-- Example
-- Delete all records in the cars table.

DELETE
FROM cars;

-- Result
-- DELETE 3


-- TRUNCATE TABLE
-- Because we omit the WHERE clause in the DELETE statement above, all records will be deleted from the cars table.
-- The same would have been achieved by using the TRUNCATE TABLE statement.

TRUNCATE TABLE cars;

