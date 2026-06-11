-- L'elenco dei Contatti: Seleziona il nome (first_name), il cognome (last_name) e l'email di tutti i clienti della tabella customer.
SELECT first_name, last_name,email 
FROM customer;


-- Catalogo Rapido: Dalla tabella film, estrai solo i titoli e la descrizione dei film.
SELECT title, description
FROM film;

-- Identità degli Attori: Mostra solo l'ID (actor_id) e il nome (first_name) di tutti gli attori.
SELECT actor_id, first_name
FROM actor;

-- Clienti VIP: Trova nome e cognome dei clienti che hanno l'ID numero 5, 10, 15 e 20.
SELECT  first_name,last_name,customer_id 
FROM customer
WHERE customer_id IN (5, 10, 15, 20); -- IN per controllare piu valori

-- Film per Bambini: Seleziona il titolo e la durata (length) di tutti i film che hanno un rating uguale a 'G'.
SELECT title, length,rating 
FROM film
WHERE rating = 'G'; -- stringhe apici singoli

-- Spese Contenute: Dalla tabella payment, trova tutti i pagamenti che hanno un importo (amount) superiore a 10 dollari.
SELECT *
FROM payment 
WHERE amount > 10;
-- x-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------x
-- Ordine Alfabetico: Estrai tutti i cognomi dei clienti in ordine alfabetico (dalla A alla Z).
SELECT last_name
FROM customer
ORDER BY last_name ASC  ;
-- Recenti ma economici: Trova i film con rental_duration uguale a 3, ordinandoli per replacement_cost dal più caro al meno caro.
SELECT title,rental_duration, replacement_cost 
FROM film
WHERE rental_duration= 3
ORDER BY replacement_cost DESC;
-- I 10 Film più brevi: Trova i titoli e la durata dei 10 film più corti presenti in catalogo.
SELECT title, length
FROM film
ORDER BY length ASC
LIMIT 10 ;
-- Ultimi pagamenti: Trova gli ultimi 5 pagamenti effettuati (ordinando per payment_id o payment_date in modo decrescente).
SELECT *
FROM payment
ORDER BY payment_date DESC
LIMIT 5;
-- Shopping mirato: Seleziona il titolo e il costo di sostituzione dei 3 film più economici che hanno una durata superiore a 120 minuti.
SELECT title, replacement_cost
FROM film
WHERE length > 120
ORDER BY replacement_cost ASC 
LIMIT 3 ;


-- Esercizio 1: "Il Catalogo Premium per Adulti"
-- Scenario: Il gestore vuole promuovere i film più lunghi e costosi, ma solo quelli con un rating specifico per un pubblico adulto (NC-17) o per adolescenti accompagnati (R).

-- Obiettivo: Trova i titoli, la durata e il costo di noleggio dei film che hanno un rating di 'NC-17' oppure 'R'.

-- Difficoltà: Devono durare più di 150 minuti e avere un costo di noleggio superiore a 2.99.

-- Ordinamento: Mostra i risultati dai più lunghi ai più brevi. Se due film hanno la stessa durata, falli apparire in ordine alfabetico per titolo.

-- Limite: Mostra solo i primi 20 risultati.

-- Suggerimento per la classe: Ricordate di usare le parentesi tonde se combinate AND e OR per essere sicuri della precedenza logica!
SELECT title,length,rental_rate
FROM film
WHERE (rating IN ('NC-17', 'R')) 
AND ( length>150)
AND (rental_rate>2.99)
ORDER BY length DESC, title ASC
LIMIT 20;
-- Esercizio 2: "Analisi Perdite e Sostituzioni"
-- Scenario: Dobbiamo identificare i film che sono "rischiosi" per il negozio: quelli che costano molto da ricomprare se persi, ma che rendono pochissimo quando vengono noleggiati.

-- Obiettivo: Seleziona titolo, rental_rate (prezzo noleggio) e replacement_cost (costo sostituzione).

-- Difficoltà: Filtra i film che hanno un costo di sostituzione superiore a 25.00 E un prezzo di noleggio inferiore a 1.00. Inoltre, il film deve avere una durata (length) compresa tra 60 e 120 minuti.

-- Ordinamento: Ordina i risultati per il costo di sostituzione più alto (dal più caro al meno caro).

-- Limite: Prendi solo i primi 10. BETWEEN

SELECT title,rental_rate,replacement_cost
FROM film
WHERE (replacement_cost > 25.00) 
AND (rental_rate < 1.00) 
AND (length BETWEEN 60 AND 120)
ORDER BY replacement_cost DESC
LIMIT 10;

-- Specialisti di Robot: Trova i titoli di tutti i film che contengono la parola "Robot" nella loro descrizione.
SELECT title
FROM film
WHERE description LIKE "%Robot%";
-- Iniziali Postali: Trova tutti i nomi delle città (tabella city) che iniziano con la lettera "S" e finiscono con la lettera "a".
SELECT city
FROM city
WHERE city LIKE "S%A";

-- Esclusioni: Mostra i titoli dei film che non iniziano con la lettera "A".
SELECT title
FROM film
WHERE title NOT LIKE "A%";

-- Il censimento degli 'Ed': Quanti attori nel database si chiamano "Ed" (nome esatto) o hanno un nome che inizia con "Ed" (es. Edward, Edwin)?
SELECT COUNT(*) AS numero
FROM actor
WHERE first_name LIKE "Ed%";
-- Genere Documentario: Conta quanti film hanno la parola "Documentary" nella loro descrizione.
SELECT COUNT(*) AS numero
FROM film
WHERE description LIKE "%Documentary%";
-- Email Professionali: Quanti clienti hanno un'indirizzo email che finisce con .org?
SELECT COUNT(*) AS numero
FROM customer
WHERE email LIKE "%.org";
-- Nomi Comuni: Quanti attori hanno un cognome che inizia con la lettera "M"?
SELECT COUNT(*) AS numero
FROM actor
WHERE last_name LIKE "M%";

-- Budget per i Dinosauri: Qual è il costo totale di sostituzione (replacement_cost) di tutti i film che contengono la parola "Dinosaur" nel titolo?
SELECT SUM(replacement_cost) AS totale
FROM film
WHERE title LIKE "%Dinosaur%";

-- La media dei "Action": Qual è la durata media (length) di tutti i film che hanno la parola "Action" nella loro descrizione?
SELECT AVG(length) AS media_durata
FROM film
WHERE description LIKE "%Action%";

-- Estremi Fantastici: Trova la durata del film più corto e di quello più lungo tra quelli che hanno la parola "Epic" nella descrizione.
SELECT MIN(length) AS piu_corto,
       MAX(length) AS piu_lungo
FROM film
WHERE description LIKE "%Epic%";

-- Incassi Parziali: Dalla tabella payment, calcola la somma totale (amount) degli incassi avvenuti nel mese di Maggio (usa payment_date LIKE '2005-05%').
SELECT SUM(amount) AS totale_incassi
FROM payment
WHERE payment_date LIKE "2005-05%"; 

-- Analisi Magazzino: Per ogni tipologia di rating (G, PG, ecc.), trova il costo di sostituzione (replacement_cost) più alto e quello più basso.
SELECT rating,
       MIN(replacement_cost) AS costo_minimo,
       MAX(replacement_cost) AS costo_massimo
FROM film
GROUP BY rating;
-- Fedeltà Clienti: Vai sulla tabella payment e calcola quanto ha speso in totale (SUM) ogni cliente (customer_id). Ordina i risultati per far vedere prima chi ha speso di più.
SELECT customer_id,
       SUM(amount) AS totale_speso
FROM payment
GROUP BY customer_id
ORDER BY totale_speso DESC;
-- Durata dei Noleggi: Per ogni possibile durata di noleggio (rental_duration), conta quanti film abbiamo in catalogo.
SELECT rental_duration,
       COUNT(*) AS numero_film
FROM film
GROUP BY rental_duration;
-- Film per "Famiglie": Trova il numero di film per ogni rating, ma considera solo i film che hanno un costo di noleggio (rental_rate) inferiore a 1.00$.
SELECT
	rating,COUNT(*) AS numero_film
FROM 
	film
WHERE 
	rental_rate<1.00
GROUP BY 
	rating;
-- Città che iniziano per A: Vai sulla tabella city. Conta quante città ci sono per ogni nazione (country_id), ma solo per le città il cui nome inizia con la lettera "A".
SELECT
    country_id,
    COUNT(*) AS numero_citta
FROM 
	city
WHERE city LIKE "A%"
GROUP BY 
    country_id;
-- Incassi di Maggio: Nella tabella payment, calcola l'incasso totale per ogni dipendente (staff_id),
-- considerando però solo i pagamenti avvenuti nel mese di Maggio (usa payment_date LIKE '2005-05%').
SELECT staff_id,
       SUM(amount) AS incasso_totale
FROM payment
WHERE payment_date LIKE "2005-05%"
GROUP BY staff_id;

-- Matrice Prezzi/Rating: Calcola la durata media dei film 
-- raggruppandoli prima per rating e poi per rental_rate.
SELECT
	rating,
	rental_rate,
	AVG(length) AS durata_media
FROM 
	film
GROUP BY 
	rating,
	rental_rate	
    ORDER BY rating;

-- Gestione Store: Nella tabella customer, 
-- conta quanti clienti ci sono per ogni negozio (store_id) 
-- e, dentro ogni negozio, quanti sono attivi 
-- e quanti inattivi (colonna active).
SELECT 
	store_id,
	active,
	COUNT(customer_id) AS numero_clienti     
FROM 
	customer
GROUP BY store_id, active
ORDER BY store_id;

-- Analisi Noleggi: Per ogni rental_duration (durata del noleggio),
--  conta quanti film ci sono divisi per rating.
SELECT rental_duration,
       rating,
       COUNT(*) AS numero_film
FROM 
	film
GROUP BY 
	rental_duration, 
    rating;
/*
Esercizio 1: "L'Anomalia dei Pagamenti di Maggio"
Scenario: L'amministrazione ha notato delle discrepanze negli incassi. 
Vogliono un report dei clienti che, nel solo mese di Maggio 2005, hanno effettuato più di 1 transazione con lo stesso dipendente, 
spendendo in totale una media superiore a 4.00$ per transazione.

Tabella: payment

Requisiti:

Filtra solo i pagamenti del mese di Maggio 2005 (usa LIKE o DATE()).

Raggruppa per cliente (customer_id) E per dipendente (staff_id).

Calcola il numero di transazioni e la media degli importi (arrotondata a 2 decimali).

Mostra solo i gruppi che hanno più di 1 transazione E una media superiore a 4.00$.

Ordina per la media più alta. 
*/
SELECT customer_id,
       staff_id,
       COUNT(*) AS numero_transazioni,
       ROUND(AVG(amount), 2) AS media_importo
FROM payment
WHERE payment_date LIKE '2005-05%'
GROUP BY customer_id, staff_id
HAVING COUNT(*) > 1
   AND AVG(amount) > 4.00
ORDER BY media_importo DESC;
/*
Esercizio 2: "Caccia all'Attore per il Remake"
Scenario: Un regista cerca attori per un nuovo film. Vuole analizzare quelli che hanno nomi "particolari" e che hanno lavorato molto, ma solo in certe fasce.

Tabelle: actor e film_actor (da usare separatamente)

Parte A (Tabella actor): Trova tutti gli attori il cui nome completo (CONCAT) è più lungo di 12 caratteri, 
inizia per 'A', 'B' o 'C' e la cui terza lettera del nome sia una 'R'.

Parte B (Tabella film_actor): Usando solo film_actor, trova gli ID degli attori (actor_id) che hanno recitato in più di 25 film,
ma escludi dalla conta i film che hanno un ID compreso tra 1 e 100.

Ordinamento: Ordina i risultati per l'ID dell'attore in modo decrescente.

*/
-- parte A
-- Parte A
SELECT actor_id,
       CONCAT(first_name, ' ', last_name) AS nome_completo
FROM actor
WHERE LENGTH(CONCAT(first_name, last_name)) > 12
  AND (
       first_name LIKE 'A%'
       OR first_name LIKE 'B%'
       OR first_name LIKE 'C%'
      )
  AND first_name LIKE '__R%';

-- parte B
SELECT actor_id,
       COUNT(*) AS numero_film
FROM film_actor
WHERE film_id NOT BETWEEN 1 AND 100
GROUP BY actor_id
HAVING COUNT(film_id) > 25
ORDER BY actor_id DESC;
/*
Esercizio 3: "Analisi Strategica del Catalogo Premium"
Scenario: Il magazzino deve decidere quali film dismettere. Vogliono un report sui film che sono "costosi da rimpiazzare" ma che non rendono abbastanza.

Tabella: film

Obiettivo: Per ogni combinazione di rating e rental_duration, vogliamo vedere delle statistiche avanzate.

Requisiti:

Considera solo i film che hanno la parola "Saga", "Dragon" o "Knight" nella descrizione.

Mostra il rating, la rental_duration e il gap di costo (ovvero la differenza tra il MAX(replacement_cost) e il MIN(replacement_cost) di quel gruppo).

Aggiungi il conteggio dei film e la durata media (length).

Filtro Finale: Mostra solo i gruppi che hanno una durata media del film superiore a 100 minuti.

Ordina per il "gap di costo" dal più alto al più basso.
*/
SELECT rating,
       rental_duration,
       (MAX(replacement_cost) - MIN(replacement_cost)) AS gap_costo,
       COUNT(*) AS numero_film,
       AVG(length) AS durata_media
FROM film
WHERE description LIKE '%Saga%'
   OR description LIKE '%Dragon%'
   OR description LIKE '%Knight%'
GROUP BY rating, rental_duration
HAVING AVG(length) > 100
ORDER BY gap_costo DESC;

/*
Esercizio 1 — JOIN di base (Customer / Payment)

Tabelle: customer, payment. Relazione: customer.customer_id = payment.customer_id.

Traccia 1.1 – INNER JOIN
Visualizza l'elenco dei clienti che hanno effettuato almeno un pagamento.
Per ciascuno mostra: nome e cognome del cliente, data del pagamento, importo.

Traccia 1.2 – LEFT JOIN
Visualizza tutti i clienti, inclusi quelli che non hanno mai effettuato pagamenti.
Per ciascuno mostra: nome e cognome, data del pagamento (se presente), importo (se presente).

Traccia 1.3 – RIGHT JOIN
Visualizza tutti i pagamenti, anche quelli che non hanno un cliente associato (caso anomalo).
Per ciascuno mostra: nome del cliente (se esiste), data del pagamento, importo.
*/
-- Traccia 1.1
SELECT 
	first_name,
	last_name,
	payment_date,
	amount
FROM customer
INNER JOIN
	payment ON customer.customer_id= payment.customer_id;

-- Traccia 1.2
SELECT 
	first_name,
	last_name,
	payment_date,
	amount
FROM customer
LEFT JOIN payment
	ON customer.customer_id= payment.customer_id;


-- Traccia 1.3
SELECT 
	first_name,
	last_name,
	payment_date,
	amount
FROM customer
RIGHT JOIN payment
	ON customer.customer_id= payment.customer_id;
/*
Esercizio 2 — Report vendite (Customer / Payment / Rental)

Tabelle: customer, payment, rental, address. Relazione: customer.customer_id = payment.customer_id = rental.customer_id.

Traccia 2.1 – INNER JOIN
Elenca i clienti attivi, cioè quelli che hanno effettuato almeno un pagamento. Per ciascuno mostra:

nome e cognome del cliente
numero totale di pagamenti effettuati
somma totale degli importi pagati
*/
SELECT c.first_name,
       c.last_name,
       COUNT( p.payment_id) AS numero_pagamenti,
       SUM(p.amount) AS totale_speso
FROM customer c
INNER JOIN payment p
ON c.customer_id = p.customer_id
GROUP BY c.customer_id,
         c.first_name,
         c.last_name;/*
Traccia 2.2 – LEFT JOIN + IS NULL
Elenca i clienti inattivi, cioè quelli che non hanno mai effettuato pagamenti. Per ciascuno mostra:

nome e cognome del cliente
indirizzo di residenza
*/
SELECT c.first_name,
       c.last_name,
       a.address
FROM customer c
LEFT JOIN payment p
ON c.customer_id = p.customer_id
INNER JOIN address a
ON c.address_id = a.address_id
WHERE p.payment_id IS NULL;
/*
Traccia 2.3 – RIGHT JOIN + IS NULL
Individua i noleggi orfani, cioè noleggi presenti in tabella ma senza un cliente valido associato. Per ciascuno mostra:

ID del noleggio
data del noleggio
importo del pagamento associato (se presente)
cliente = NULL 
*/
SELECT r.rental_id,
       r.rental_date,
       p.amount,
       c.customer_id
FROM customer c
RIGHT JOIN rental r
ON c.customer_id = r.customer_id
LEFT JOIN payment p
ON r.rental_id = p.rental_id
WHERE c.customer_id IS NULL; 
/*
Esercizio 3 — Film e Noleggi con filtri (Film / Inventory / Rental / Category / Actor / Store / Address)

Catena principale: film → inventory → rental. Tabelle di supporto: film_category, category, film_actor, actor, store, address.

Traccia 3.1 – INNER JOIN + WHERE + LIKE
Visualizza i film noleggiati almeno una volta, mostrando: titolo, nome completo dell'attore, data del noleggio, ID del negozio.
Includi solo i film in cui il nome completo dell'attore contiene la stringa "Allen" (case-insensitive).
*/
SELECT f.title,
       CONCAT(a.first_name, ' ', a.last_name) AS attore,
       r.rental_date,
       i.store_id
FROM film f
INNER JOIN inventory i
ON f.film_id = i.film_id
INNER JOIN rental r
ON i.inventory_id = r.inventory_id
INNER JOIN film_actor fa
ON f.film_id = fa.film_id
INNER JOIN actor a
ON fa.actor_id = a.actor_id
WHERE CONCAT(a.first_name, ' ', a.last_name) LIKE '%Allen%';
/*
Traccia 3.2 – LEFT JOIN + WHERE + BETWEEN
Visualizza tutti i film, anche quelli senza noleggi registrati, mostrando: titolo, anno di uscita, prezzo di noleggio, data del noleggio (se presente).
Filtra per release_year compreso tra 2004 e 2006.
*/
SELECT f.title,
       f.release_year,
       f.rental_rate,
       r.rental_date
FROM film f
LEFT JOIN inventory i
ON f.film_id = i.film_id
LEFT JOIN rental r
ON i.inventory_id = r.inventory_id
WHERE f.release_year BETWEEN 2004 AND 2006;
/*
Traccia 3.3 – INNER JOIN + WHERE + IN
Visualizza i film noleggiati nei negozi con store_id IN (1, 2).
Per ciascun gruppo mostra: titolo, ID del negozio, numero totale di noleggi, ricavo totale (numero noleggi × rental_rate).
*/
SELECT f.title,
       i.store_id,
       COUNT(r.rental_id) AS totale_noleggi,
       COUNT(r.rental_id) * f.rental_rate AS ricavo_totale
FROM film f
INNER JOIN inventory i
ON f.film_id = i.film_id
INNER JOIN rental r
ON i.inventory_id = r.inventory_id
WHERE i.store_id IN (1, 2)
GROUP BY f.title,
         i.store_id,
         f.rental_rate;
/*
Traccia 3.4 – RIGHT JOIN + WHERE + LIKE + BETWEEN
Visualizza tutti i noleggi, anche quelli che fanno riferimento a copie non più collegate a un film in catalogo (caso anomalo).
Mostra: titolo (se esiste), data del noleggio, prezzo, ID inventario.
Includi solo i noleggi:

avvenuti tra 2005-06-01 e 2005-08-31
presso negozi il cui indirizzo contiene la parola "Main" (case-insensitive)

*/
SELECT f.title,
       r.rental_date,
       f.rental_rate,
       i.inventory_id
FROM film f
RIGHT JOIN inventory i
ON f.film_id = i.film_id
RIGHT JOIN rental r
ON i.inventory_id = r.inventory_id
INNER JOIN store s
ON i.store_id = s.store_id
INNER JOIN address a
ON s.address_id = a.address_id
WHERE r.rental_date BETWEEN '2005-06-01' AND '2005-08-31'
  AND a.address LIKE '%Main%';
/*
Traccia 3.5 – INNER JOIN + WHERE combinato
Mostra titolo, genere, prezzo e data del noleggio dei film che soddisfano tutte le seguenti condizioni:

genere IN ('Action', 'Horror', 'Comedy')
release_year successivo al 2004
noleggiati in un negozio il cui indirizzo contiene "Main" (case-insensitive)

Ordina dal noleggio più recente al più vecchio.
*/SELECT f.title,
       c.name AS genere,
       f.rental_rate,
       r.rental_date
FROM film f
INNER JOIN film_category fc
ON f.film_id = fc.film_id
INNER JOIN category c
ON fc.category_id = c.category_id
INNER JOIN inventory i
ON f.film_id = i.film_id
INNER JOIN rental r
ON i.inventory_id = r.inventory_id
INNER JOIN store s
ON i.store_id = s.store_id
INNER JOIN address a
ON s.address_id = a.address_id
WHERE c.name IN ('Action', 'Horror', 'Comedy')
  AND f.release_year > 2004
  AND a.address LIKE '%Main%'
ORDER BY r.rental_date DESC;
-- Trovare tutti i titoli dei film noleggiati dal cliente con cognome 'HUNT'.
SELECT DISTINCT f.title
FROM customer c
INNER JOIN rental r
    ON c.customer_id = r.customer_id
INNER JOIN inventory i
    ON r.inventory_id = i.inventory_id
INNER JOIN film f
    ON i.film_id = f.film_id
WHERE c.last_name = 'HUNT';
-- --- FACILE ---

-- Elencare i titoli dei film della categoria 'Sci-Fi' che hanno un rating 'PG'.
SELECT f.title
FROM film f
INNER JOIN film_category fc
    ON f.film_id = fc.film_id
INNER JOIN category c
    ON fc.category_id = c.category_id
WHERE c.name = 'Sci-Fi'
  AND f.rating = 'PG';
-- Calcolare il totale degli incassi (revenue) generati da ciascuno dei due punti vendita (Store).
SELECT s.store_id,
       SUM(p.amount) AS incasso_totale
FROM store s
INNER JOIN staff st
    ON s.store_id = st.store_id
INNER JOIN payment p
    ON st.staff_id = p.staff_id
GROUP BY s.store_id;
-- Trovare i titoli di tutti i film che sono presenti nel database ma che non sono mai stati noleggiati
SELECT f.title
FROM film f
LEFT JOIN inventory i
    ON f.film_id = i.film_id
LEFT JOIN rental r
    ON i.inventory_id = r.inventory_id
WHERE r.rental_id IS NULL;

-- Trovare tutte le coppie di attori che hanno recitato insieme in più di 3 film. Visualizza i nomi di entrambi gli attori e il numero di film fatti insieme.

SELECT 
    CONCAT(a1.first_name, ' ', a1.last_name) AS attore_1,
    CONCAT(a2.first_name, ' ', a2.last_name) AS attore_2,
    COUNT(*) AS film_insieme
FROM film_actor fa1

INNER JOIN film_actor fa2
    ON fa1.film_id = fa2.film_id
   AND fa1.actor_id < fa2.actor_id

INNER JOIN actor a1
    ON fa1.actor_id = a1.actor_id

INNER JOIN actor a2
    ON fa2.actor_id = a2.actor_id

GROUP BY 
    fa1.actor_id,
    fa2.actor_id,
    attore_1,
    attore_2

HAVING COUNT(*) > 3

ORDER BY film_insieme DESC;
-- Trovare il fatturato totale (total revenue) generato dai clienti che vivono in India, suddiviso per categoria di film.
SELECT 
    c.name AS categoria,
    SUM(p.amount) AS fatturato_totale
FROM country co

INNER JOIN city ci
    ON co.country_id = ci.country_id

INNER JOIN address a
    ON ci.city_id = a.city_id

INNER JOIN customer cu
    ON a.address_id = cu.address_id

INNER JOIN payment p
    ON cu.customer_id = p.customer_id

INNER JOIN rental r
    ON p.rental_id = r.rental_id

INNER JOIN inventory i
    ON r.inventory_id = i.inventory_id

INNER JOIN film_category fc
    ON i.film_id = fc.film_id

INNER JOIN category c
    ON fc.category_id = c.category_id

WHERE co.country = 'India'

GROUP BY c.name

ORDER BY fatturato_totale DESC;

-- Trovare i primi 3 attori che hanno generato il maggior incasso totale (revenue) per i noleggi effettuati da clienti che risiedono nella città di Londra.
SELECT 
    CONCAT(a.first_name, ' ', a.last_name) AS attore,
    SUM(p.amount) AS incasso_totale
FROM city ci

INNER JOIN address ad
    ON ci.city_id = ad.city_id

INNER JOIN customer cu
    ON ad.address_id = cu.address_id

INNER JOIN payment p
    ON cu.customer_id = p.customer_id

INNER JOIN rental r
    ON p.rental_id = r.rental_id

INNER JOIN inventory i
    ON r.inventory_id = i.inventory_id

INNER JOIN film_actor fa
    ON i.film_id = fa.film_id

INNER JOIN actor a
    ON fa.actor_id = a.actor_id

WHERE ci.city = 'London'

GROUP BY a.actor_id,
         attore

ORDER BY incasso_totale DESC

LIMIT 3;