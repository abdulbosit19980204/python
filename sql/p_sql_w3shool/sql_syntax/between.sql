-- PostgreSQL BETWEEN Operator

-- BETWEEN
-- The BETWEEN operator selects values within a given range. The values can be numbers, text, or dates
-- The BETWEEN operator is inclusive: begin and end values are included.

-- Example
-- Select all products with a price between 10 and 15.

SELECT *
FROM products
WHERE price BETWEEN 10 AND 15;

-- BETWEEN Text Values
-- The BETWEEN operator can also be used on text values.
-- The result returns all records that are alphabetically between the specified values.

-- Example:
-- SELECT all products between 'Pavlova' and 'Tofu'

SELECT *
FROM products
WHERE product_name BETWEEN 'Pavlova' AND 'Tofu';

-- If we add an ORDER BY clause to the example above, it will be a bit easier to read:

-- Example:
-- Same example as above, but we sort it by product_name:
SELECT *
FROM products
WHERE product_name BETWEEN 'Pavlova' AND 'Tofu'
ORDER BY product_name;

-- Between Date Values
-- The BETWEEN operator can also be used on date values.

-- Example
-- Select all orders between 12. of April 2023 and 5. May 2023

SELECT *
FROM orders
WHERE order_date BETWEEN '2023-04-12' AND '2023-05-05';

