-- PostgreSQL COUNT Function

-- COUNT
-- The COUNT() function returns the number of rows that matches a specified criterion.

-- If the specified criterion is a column name, the COUNT() function returns the number of columns with that name.

-- Example
-- Return the number of customers from the customers table:
SELECT COUNT(customer_id)
FROM customers;

-- Note: NULL values are not counted.
-- By specifying a WHERE clause, you can e.g return the number of customer that comes from London

-- Example
-- Return the number of customers  from London

SELECT COUNT(customer_id)
FROM customers
WHERE city = 'London';

