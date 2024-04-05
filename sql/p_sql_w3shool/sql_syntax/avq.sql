-- PostgreSQL AVG Function

-- AVG
-- The AVG() function returns the average value of a numeric column.

-- Example
-- Return the average price of all the products in the products table.

SELECT AVG(price)
FROM products;

-- Note: NULL values are ignored.

-- With 2 Decimals
-- The above example returned the average price of all products, the result was 28.8663636363636364.
-- We can use the ::NUMERIC operator to round the average price to a number with 2 decimals.

-- Example

-- Return the average price of all the products, rounded to 2 decimals.
SELECT AVG(price)::NUMERIC(10, 2)
FROM products;

