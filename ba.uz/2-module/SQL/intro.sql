CREATE TABLE post
(
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


