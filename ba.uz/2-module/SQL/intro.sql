CREATE TABLE post
(
    id           serial primary key,
    title        varchar(255) not null,
    description  text         not null,
    created_at   timestamp default CURRENT_TIMESTAMP,
    is_published boolean   default TRUE
);

INSERT INTO post(title, description)
VALUES ('A', 'Description');

SELECT *
FROM post
where is_published = TRUE
ORDER BY title
;

DROP TABLE post;

SELECT *
FROM post
WHERE title = 'A'
ORDER BY id DESC
LIMIT 1;


UPDATE post
SET title='C'
WHERE id = 3;

SELECT *
FROM post
WHERE id = 3;


SELECT *
FROM post
ORDER BY id;

DELETE
FROM post
WHERE id = 24;

CREATE TABLE student
(
    id         serial primary key,
    name       VARCHAR(255),
    age        INT,
    university VARCHAR(255)
);


INSERT INTO student (name, age, university)
VALUES ('Abdulbosit', 26, 'TUIT'),
       ('Diyorbek', 20, 'NamDU'),
       ('Shokirali', 36, 'MGU');

SELECT *
FROM student;

SELECT *
FROM student
WHERE age = (SELECT MAX(age) FROM student);

SELECT *
FROM student
ORDER BY age DESC
LIMIT 1;

