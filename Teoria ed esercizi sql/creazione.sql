-- crea nuovo db
CREATE DATABASE test;

-- usa il nuovo db
USE test;



/** 
tipi di dato:
	INT (4 byte)
    BIGINT (8 byte)
    FLOAT/DOUBLE
    BOOLEAN
    VARCHAR
    TEXT
    DATE
    DATETIME
    ENUM
    JSON
**/

-- PRIMARY KEY

CREATE TABLE project (
	id INT PRIMARY KEY AUTO_INCREMENT, -- PRIMARY KEY = valore unico / AUTO_INCREMENT = ad ogni aggiunda il db da solo fa id+1
    title VARCHAR(100),
    topic VARCHAR(50)
);

-- VINCOLI
CREATE TABLE user (
	id INT PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(100) NOT NULL, -- deve esserci
    email VARCHAR(100) NOT NULL UNIQUE, -- deve esserci e non posso avere più account con stessa mail
    phone VARCHAR(20) UNIQUE -- no più account con stesso numero
);

CREATE TABLE orders (
	order_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    delivered BOOL DEFAULT False, -- DEFAULT COME IN PYTHON
    payment INT,
    CONSTRAINT check_payment CHECK (payment > 3) -- POSSO INSERIRE VINCOLI
);

-- FOREIGN KEY
CREATE TABLE author (
	author_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(255) NOT NULL
);

CREATE TABLE book (
	book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(150) NOT NULL,
    
    author_id INT, -- stesso nome della primary key della tabella a cui collegare
    
    FOREIGN KEY (author_id) REFERENCES author(author_id) -- prima la variabile di partenza e poi la variabile di arrivo e la tabella
);
CREATE DATABASE test_biblioteca;
USE test_biblioteca;