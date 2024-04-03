-- PostgreSQL Select Data

-- SELECT DATA
-- To retrieve data from data base, we use the SELECT statement.

-- Specify Columns!
-- By specifying the column names, we can choose which columns to select.
SELECT customer_name, country
FROM customers;

-- Return All Columns!
-- Specify a * instead of  the column names to select all columns:
SELECT *
FROM customers;
