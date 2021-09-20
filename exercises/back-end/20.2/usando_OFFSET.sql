-- LIMIT OFFSET - DB sakil
SELECT * FROM sakila.rental;

-- Pulando n linhas com OFFSET
SELECT * FROM sakila.rental LIMIT 10 OFFSET 3;

-- Trazendo resultado a partir de JOHNNY
SELECT * FROM sakila.actor LIMIT 6 OFFSET 4;