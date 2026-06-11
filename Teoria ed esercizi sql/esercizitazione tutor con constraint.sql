/*
Il cliente richiede lo sviluppo del backend per un'applicazione di gestione attività (To-Do List) multi-utente. L'app deve permettere agli utenti di registrarsi, creare diverse liste (es. "Lavoro", "Personale", "Spesa") e aggiungere attività specifiche a ciascuna lista.

2. Fase 1: Data Definition Language (DDL)
Obiettivo: Creare lo scheletro del database.

Scrivi il codice SQL per creare le seguenti tre tabelle, rispettando i vincoli indicati:

users:

user_id: Chiave primaria, intero, auto-incrementale.

username: Testo (50), obbligatorio, unico.

email: Testo (100), obbligatorio, unico.

created_at: Data e ora, default al momento dell'inserimento.

lists:

list_id: Chiave primaria, intero, auto-incrementale.

user_id: Chiave esterna verso users.

title: Testo (100), obbligatorio.

Regola di integrità: Se un utente viene eliminato, tutte le sue liste devono essere rimosse automaticamente.

tasks:

task_id: Chiave primaria, intero, auto-incrementale.

list_id: Chiave esterna verso lists.

description: Testo lungo, obbligatorio.

status: Testo, default 'pending'.

due_date: Data (può essere nulla).

Regola di integrità: Se una lista viene eliminata, tutte le task al suo interno devono essere rimosse automaticamente.

3. Fase 2: Data Manipulation Language (DML)
Obiettivo: Popolare e gestire i dati.

Esegui le seguenti operazioni in ordine:

Registrazione: Inserisci almeno 2 utenti nel sistema.

Organizzazione: Crea 2 liste per il primo utente e 1 lista per il secondo.

Pianificazione: Aggiungi 3 task alla prima lista (una con una data di scadenza passata, una futura e una senza data).

Avanzamento: Aggiorna lo stato di una task da 'pending' a 'completed'.

Pulizia: Elimina una task specifica identificandola tramite il suo ID.

4. Fase 3: Data Query Language (DQL)
Obiettivo: Estrarre informazioni utili.

Scrivi le query per ottenere:

Tutte le task di una specifica lista, ordinate per due_date.

Tutte le email degli utenti che hanno almeno una task con stato 'pending'.

Il conteggio delle task completate per ogni lista (usa GROUP BY).

A. Vincoli di Controllo Avanzati
Aggiungi (o modifica) la tabella tasks inserendo un vincolo CHECK sulla colonna status. Lo stato deve accettare solo i seguenti tre valori: 'pending', 'in_progress', 'completed'. Nessun altro testo deve essere ammesso.

B. Gestione delle Priorità
Aggiungi una colonna priority alla tabella tasks (tipo intero). Imposta un vincolo DEFAULT a 3 (priorità media) e un CHECK affinché il valore sia sempre compreso tra 1 (massima) e 5 (minima).

C. La Tabella "Tags" (Relazione N:M)
Questa è la sfida definitiva. Crea un sistema di Tag (es. "Urgente", "Casa", "Computer"):

Crea la tabella tags (tag_id, name).

Crea una tabella ponte task_tags per permettere a una task di avere più tag e a un tag di essere associato a più task.

Configura le FOREIGN KEY con ON DELETE CASCADE affinché la cancellazione di un tag o di una task pulisca correttamente la tabella ponte.
*/
-- DDL TABELLE

CREATE DATABASE gestione_attività;

-- usa il nuovo db
USE gestione_attività;
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE lists (
    list_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(100) NOT NULL,
    CONSTRAINT fk_lists_users
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);

CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    list_id INT,
    description TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    due_date DATE,
    priority INT DEFAULT 3,

    CONSTRAINT fk_tasks_lists
        FOREIGN KEY (list_id)
        REFERENCES lists(list_id)
        ON DELETE CASCADE,

    CONSTRAINT chk_status
        CHECK (status IN ('pending', 'in_progress', 'completed')),

    CONSTRAINT chk_priority
        CHECK (priority BETWEEN 1 AND 5)
);

CREATE TABLE tags (
    tag_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE task_tags (
    task_id INT,
    tag_id INT,

    PRIMARY KEY (task_id, tag_id),

    CONSTRAINT fk_tt_task
        FOREIGN KEY (task_id)
        REFERENCES tasks(task_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_tt_tag
        FOREIGN KEY (tag_id)
        REFERENCES tags(tag_id)
        ON DELETE CASCADE
);


-- DML (INSERIMENTI)


INSERT INTO users (username, email)
VALUES 
('mario', 'mario@mail.com'),
('luigi', 'luigi@mail.com');

INSERT INTO lists (user_id, title)
VALUES 
(1, 'Lavoro'),
(1, 'Personale'),
(2, 'Spesa');

INSERT INTO tasks (list_id, description, status, due_date)
VALUES
(1, 'Task scaduta', 'pending', '2024-01-01'),
(1, 'Task futura', 'pending', '2027-01-01'),
(1, 'Task senza data', 'pending', NULL);

INSERT INTO tags (name)
VALUES ('Urgente'), ('Casa'), ('Computer');

INSERT INTO task_tags (task_id, tag_id)
VALUES (1, 1), (2, 2);


-- UPDATE / DELETE


UPDATE tasks
SET status = 'completed'
WHERE task_id = 1;

DELETE FROM tasks
WHERE task_id = 2;


-- DQL (QUERY)


SELECT *
FROM tasks
WHERE list_id = 1
ORDER BY due_date ASC;

SELECT DISTINCT u.email
FROM users u
JOIN lists l ON u.user_id = l.user_id
JOIN tasks t ON l.list_id = t.list_id
WHERE t.status = 'pending';

SELECT l.list_id, l.title, COUNT(t.task_id) AS completed_tasks
FROM lists l
LEFT JOIN tasks t 
    ON l.list_id = t.list_id 
    AND t.status = 'completed'
GROUP BY l.list_id, l.title;