-- PostgreSQL WHERE - FILTER Data

-- Filter Records

-- The WHERE clause is used to filter records.
-- It is used to extract only those records that fulfill a specified condition.
-- If we want to return only the records where city is London, we can specify  that in the WHERE clause:

-- Example
SELECT *
FROM customers
WHERE city = 'London';

-- Text Fields vs. Numeric Fields
-- PostgreSQL requires quotes around text values
-- However, numeric fields should not be enclosed in quotes:

-- Example
SELECT *
FROM customers
WHERE customer_id = 11;


-- Quotes around numeric fields will not fail, but it is good proctise to always write numeric values with quotes.

-- Greater Than

-- Use the > operator to return all records where customer_id is greater than 80:

-- Example
SELECT *
FROM customers
WHERE customer_id > 80;


-- Quotes around numeric fields will not fail, but it is good practise to always write numeric values without quotes.

