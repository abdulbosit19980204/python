-- PostgreSQL LIKE Operator

-- LIKE

-- The LIKE operator is used in a WHERE clause to search for a specified pattern in  a column.
-- There are two wildcards often used in conjunction with the LIKE operator.

-- % - The percent sign represents zero, one or multiple characters
-- _ - The underscore sign represents one, single character

-- Starts with
-- To return records that starts with a specific letter or phrase, and the % at the end of the letter or phrase.

-- Example
-- Return all customers with a name that starts with the letter 'A':
SELECT *
FROM customers
WHERE customer_name LIKE 'A%';

-- Contains
-- To return records that contains a specific letter or phrase, add the % both before and after the letter or phrase.

-- Example
-- Return all customers with a name that contains the letter 'A':
SELECT *
FROM customers
WHERE customer_name LIKE '%A%';

-- ILIKE
-- Note: The LIKE operator is case sensitive, if you want to do a case insensitive search, use the ILIKE operator instead.

-- Example
-- Return all customers with a name that contains the letter 'A' or 'a'
SELECT *
FROM customers
WHERE customer_name ILIKE '%A%';

-- Ends with
-- To return records that ends with a specific letter or phrase, add the % before the letter or phrase.

-- Example
-- Return all customers with a name that ends with the phrase 'en':
SELECT *
FROM customers
WHERE customer_name LIKE '%en';


-- The Underscore _Wildcard

-- The _ wildcard represents a single character.
-- It can be any character or number, but each _ represents one, and only one, character.
-- Example
-- Return all customers from a city that starts with 'L' followed by one wildcard character,
-- then 'nd' and then two wildcard characters:

SELECT *
FROM customers
WHERE city LIKE 'L_nd__';

