-- PostgreSQL HAVING Clause

-- Having

-- The HAVING clause was added to SQL because the WHERE clause cannot be used with aggregate functions.
-- Aggregate function are often used with GROUP BY clauses, and by adding HAVING we can write condition like we do with
-- WHERE clause

-- Example
-- List only countries that are represented more than 5 times:

SELECT COUNT(customer_id), country
FROM customers
GROUP BY country
HAVING COUNT(customer_id) > 5;