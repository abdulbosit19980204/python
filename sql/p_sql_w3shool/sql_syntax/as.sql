-- PostgreSQL AS

-- Aliases

-- SQL aliases are used to give a table, or a column in a table, a temporary name.

-- Aliases are often used to make column names more readable.

-- An alias only exists for the duration of that query.
-- An alias is created with the AS keyword.

-- Example

-- Using aliases for columns:
SELECT customer_id as id
FROM customers;

-- AS is optional
-- Actually you can skip the AS keyword and get the same result

-- Example
-- Same result without AS:
SELECT customer_id id
FROM customers;

-- Concatenate Columns
-- The AS keyword is often used when two or more fields are concatenated into one.
-- To concatenate two fields use ||.

-- Example
-- Concatenate two fields and call them product:
SELECT product_name || unit AS product
FROM products;

-- Note: In the result of the example above we are missing a space between product_name and unit. To add a space when
-- concatenating, use || ' ' ||    .

-- Example
-- Concatenate, with space:
SELECT product_name || ' ' || unit AS product
FROM products;


-- Using Aliases With a space character
-- If you want your alias to contain one or more spaces, like "My Greate Products", surround your alias with double quotes

-- Example
-- Surround your alias with double quotes:
SELECT product_name AS "My Greate Products"
FROM products;

