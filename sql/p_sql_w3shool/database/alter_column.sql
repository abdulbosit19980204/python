-- PostgreSQL ALTER COLUMN

-- The ALTER TABLE Statement

-- To change the data type, or the size of table column we have to use the ALTER TABLE statement.
-- The ALTER TABLE statement is used to add, delete, or modify columns in an existing table.
-- The ALTER TABLE statement is also used to add and drop various constraints on an existing table.


-- ALTER COLUMN

-- We want to change the data type of the year column of the cars table from int to varchar(4).
-- To modify a column, use the ALTER COLUMN statement and the TYPE keyword followed by the data type:

-- Example
-- Change the year column from INT to VARCHAR(4)
ALTER TABLE cars
    ALTER COLUMN year TYPE VARCHAR(4);

-- Note: Some data types cannot be converted if the column has value E.g. numbers can always be converted to text, but
-- text cannot always be converted to numbers

-- Change Maximum Allowed Characters

-- We also want to change the maximum number of characters allowed in the color column of the cars table.
-- Use the same syntax as above, use the ALTER COLUMN  statement and the TYPE keyword followed by the new data type

-- Example
-- Change the color column from VARCHAR(255) to VARCHAR(30).

ALTER TABLE cars
    ALTER COLUMN color TYPE VARCHAR(30);
