-- PostgreSQL CASE Expression

-- CASE

-- The CASE expression goes through conditions and returns a value when the first condition is meet
-- (like an if-then-else statement)

-- Once a condition is true, it will stop reading and return the result. If no conditions are true, it
-- returns the value in the ELSE clause.

-- IF there is not ELSE part and no conditions are true, it returns NULL.

-- Example
-- Return specific values if the price meets a specific condition:

SELECT product_name,
       CASE
           WHEN price < 10 THEN 'Low price product'
           WHEN price > 50 THEN 'High price product'
           ELSE
               'Normal product'
           END
FROM products;


-- With an Alias
-- When a column name is not specified for the "case" field, the parser uses case as the column name.
-- To specify a column name, add an alias after the END keyword.

-- Example
-- Same example, but with an alias for the case column:

SELECT product_name,
       CASE
           WHEN price < 10 THEN 'Low price product'
           WHEN price > 50 THEN 'High price product'
           ELSE
               'Normal product'
           END AS "price category"
FROM products;

