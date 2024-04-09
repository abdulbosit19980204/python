-- PostgreSQL CROSS JOIN

-- CROSS JOIN
-- The CROSS JOIN keyword matches ALL records from the "left" table with EACH record from the "right" table.
-- The means that all records from the "right" table will be returned for each record in the "left" table.

-- This way of joining can potentially return very large table, and you should not use it if you do not have to.
-- Let's look at an example using our dummy testproducts table:
testproduct_id |      product_name      | category_id
----------------+------------------------+-------------
              1 | Johns Fruit Cake       |           3
              2 | Marys Healthy Mix      |           9
              3 | Peters Scary Stuff     |          10
              4 | Jims Secret Recipe     |          11
              5 | Elisabeths Best Apples |          12
              6 | Janes Favorite Cheese  |           4
              7 | Billys Home Made Pizza |          13
              8 | Ellas Special Salmon   |           8
              9 | Roberts Rich Spaghetti |           5
             10 | Mias Popular Ice       |          14
(10 rows)

-- We will try join the testproducts table with the categories table:
category_id | category_name  |                       description
-------------+----------------+------------------------------------------------------------
           1 | Beverages      | Soft drinks, coffees, teas, beers, and ales
           2 | Condiments     | Sweet and savory sauces, relishes, spreads, and seasonings
           3 | Confections    | Desserts, candies, and sweet breads
           4 | Dairy Products | Cheeses
           5 | Grains/Cereals | Breads, crackers, pasta, and cereal
           6 | Meat/Poultry   | Prepared meats
           7 | Produce        | Dried fruit and bean curd
           8 | Seafood        | Seaweed and fish
(8 rows)


-- Note: The CROSS JOIN method will return ALL categories for EACH testproduct,
-- meaning that it will return 80 rows (10*8)


-- Example: Join testproducts to categories using the CROSS JOIN keyword:
SELECT testproduct_id, product_name, category_name
FROM testproducts
         CROSS JOIN categories;

