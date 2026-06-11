SELECT * FROM film;
SELECT * FROM actor;

-- Select seleziona tutti (*) o solo alcune colonne da una tabella
SELECT title, rating FROM film;

-- Selezionare record precisi della nostra tabella?
SELECT title, rating, rental_rate 
FROM film
WHERE rental_rate = 0.99;

-- Ordinare i risultati?
SELECT title, length 
FROM film
WHERE length>130
ORDER BY length DESC; -- in base alla length in modo decrescente

-- Se volessi vedere solo i top n?
SELECT title, replacement_cost, rental_duration
FROM film
WHERE (replacement_cost<20 OR length > 100)  -- seleziono solo i film che hanno replacement cost < 20
ORDER BY rental_duration ASC -- in modo crescente, dal più piccolo
LIMIT 5; -- i migliori 5

# BETWEEN, IN (...), IS NULL / IS NOT NULL

# COMANDI DI AGGREGAZIONE
-- quanti film ci sono in film?

SELECT COUNT(*) as n_film 
FROM film;

-- all conta tutte le righe (i record), 
-- se inserite una colonna conta i valori non nulli della colonna

-- SUM per sommare
SELECT SUM(replacement_cost) as spesa_totale
FROM film;

SELECT AVG(replacement_cost) as media_repalcement
FROM film;

SELECT MIN(length) as durata_minima, MAX(length) as durata_massima
FROM film;

SELECT MIN(length) as durata_minima, MAX(length) as durata_massima
FROM film
WHERE rating="PG";

-- LIKE, ci aiuta a trovare stringhe che rispettano un pattern
SELECT first_name, last_name
FROM actor
WHERE first_name LIKE "E%"; -- % = qualsiasi cosa in qualsiasi numero

SELECT title
FROM film
WHERE title LIKE "%LOVE%"; -- % = qualsiasi cosa in qualsiasi numero

SELECT first_name, last_name
FROM actor
WHERE first_name LIKE "C___"; -- _ ogni trattino è un singolo qualsiasi carattere

SELECT first_name, last_name
FROM actor
WHERE first_name NOT LIKE "C___" AND first_name LIKE "C%"; -- NOT come anti pattern

-- GROUP BY 
SELECT rating, COUNT(*) AS totale_film
FROM film
GROUP BY rating; -- select e groupby devono avere le stesse colonne, ad eccezione delle funzioni di raggruppamento

SELECT actor_id, COUNT(film_id) as numero_film
FROM film_actor
GROUP BY actor_id
ORDER BY numero_film DESC;

-- Doppio raggruppamento
-- raggruppo per il primo, dentro il raggruppamento del primo faccio un sotto raggruppamento 
-- per il secondo e per ogni sotto raggruppamento fa il count

SELECT 
	rating, rental_rate, 
    COUNT(*) as numero_film
FROM film
GROUP BY 
	rating, 
    rental_rate 
ORDER BY 
	rating, 
    rental_rate;
    
-- HAVING, in combo con groupby

SELECT customer_id, SUM(amount) as totale_speso
FROM payment
GROUP BY customer_id
HAVING totale_speso > 217;

-- Distinct, valori unici in una colonna
SELECT DISTINCT rental_rate FROM film;

-- Concat, per unire colonne
SELECT CONCAT(first_name, " ", last_name) as nome_cognome
FROM actor;

-- funzioni per le date, estrarre mese o anno su colonne di tipo datetime
SELECT MONTH(rental_date) as mese, YEAR(rental_date) as anno
FROM rental;