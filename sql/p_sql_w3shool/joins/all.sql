-- PostgreSQL ALL Operator

-- ALL
-- The ALL operator

-- *returns a Boolean value as a result
-- *returns TRUE if ALL of the sub query values meet the condition
-- *is used with SELECT, WHERE  and HAVING statements

-- ALL means that the condition will be true only if the operation is true for all values in the range

-- Example

-- List the products if ALL the records in the records order_details with quantity larger than 10.
-- Note: This will of course return FALSE because the quantity column has many different value (not only the value of 10):
SELECT product_name
FROM products
WHERE product_id = ALL (SELECT product_id
                        FROM order_details
                        WHERE quantity > 10);


