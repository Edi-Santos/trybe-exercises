-- Usando ORDER BY - DB sakila

-- Ordenando de forma alfabética:
SELECT * FROM sakila.actor
ORDER BY first_name;

-- Ordenando numericamente
SELECT * FROM sakila.payment
ORDER BY rental_id;

-- Ordenando por mais de uma coluna
SELECT * FROM sakila.payment
ORDER BY amount ASC, rental_id DESC;
