-- Primeiras queries - DB sakila
-- 1- Escreva uma query que selecione todas as colunas da tabela city
SELECT * FROM sakila.city;

-- 2- Escreva uma query que exiba apenas as colunas first_name e last_name da tabela customer
SELECT first_name, last_name FROM sakila.customer;

-- 3- Escreva uma query que exiba todas as colunas da tabela rental
SELECT * FROM sakila.rental;

-- 4- Escreva uma query que exiba o título, a descrição e a data de lançamento dos filmes registrados na tabela film ;
SELECT title, description, release_year FROM sakila.film;

-- 5- Utilize o SELECT para explorar todas as tabelas do banco de dados
SELECT * FROM sakila.actor;
SELECT * FROM sakila.address;
SELECT * FROM sakila.category;
SELECT * FROM sakila.city;
SELECT * FROM sakila.country;
SELECT * FROM sakila.customer;
SELECT * FROM sakila.film;
SELECT * FROM sakila.film_actor;
SELECT * FROM sakila.film_category;
SELECT * FROM sakila.film_text;
SELECT * FROM sakila.inventory;
SELECT * FROM sakila.language;
SELECT * FROM sakila.payment;
SELECT * FROM sakila.rental;
SELECT * FROM sakila.staff;
SELECT * FROM sakila.store;