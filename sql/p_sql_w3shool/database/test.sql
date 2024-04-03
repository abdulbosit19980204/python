SELECT *
FROM cars;
INSERT INTO cars(brand, model, year, price)
VALUES ('Chevrolet', 'Malibu', 2020, 22000),
       ('Chevrolet', 'Nexia', 2023, 9500);

ALTER TABLE cars
    ALTER COLUMN year TYPE varchar(4);

INSERT INTO cars (brand, model, year, price)
VALUES ('Chevrolet', 'Spark', 2017, 7500);

ALTER TABLE cars
    DROP COLUMN brand;

DELETE
FROM cars
where model = 'Spark';

DELETE
FROM cars;

TRUNCATE TABLE cars;
