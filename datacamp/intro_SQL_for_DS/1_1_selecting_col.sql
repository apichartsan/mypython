
SELECT name, birthdate
FROM people;

SELECT *
FROM people;

SELECT *
FROM people
LIMIT 10;

/* Often your results will include many duplicate values. If you want to select all the unique values from a column, you can use the DISTINCT keyword.

   This might be useful if, for example, you're interested in knowing which languages are represented in the films table:
*/

SELECT DISTINCT language
FROM films;


-- You can test out queries here!
SELECT COUNT(*)
FROM reviews;

-- to count the number of birth dates present in the people table (if there are some row missing)
SELECT COUNT(birthdate)
FROM people;

SELECT COUNT(DISTINCT birthdate)
FROM people;

SELECT COUNT(DISTINCT country)
FROM films;



SELECT *
FROM films
WHERE release_year = 2016;

SELECT COUNT(*)
FROM films
WHERE release_year < 2000;

SELECT title, release_year
FROM films
WHERE release_year > 2000;


SELECT *
FROM films
WHERE language = 'French';

SELECT name
FROM people
WHERE birthdate = '1974-11-11';

SELECT COUNT(*)
FROM films
WHERE language = 'Hindi';

SELECT *
FROM films
WHERE certification = 'R';


SELECT title, release_year
FROM films
WHERE language = 'Spanish'
AND release_year < 2000;

SELECT *
FROM films
WHERE language = 'Spanish'
AND release_year > 2000;

SELECT *
FROM films
WHERE language = 'Spanish'
AND release_year > 2000
AND release_year < 2010;






