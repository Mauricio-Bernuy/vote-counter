CREATE DATABASE votesdatabase;

CREATE TABLE IF NOT EXISTS votos(
	region varchar NOT NULL,
	provincia varchar NOT NULL,
	ciudad varchar NOT NULL,
	dni int PRIMARY KEY NOT NULL,
	candidato varchar NOT NULL,
	esvalido bool NOT NULL,
	consumed bool DEFAULT FALSE NOT NULL 
);

CREATE TABLE IF NOT EXISTS conteovotos(
	region varchar NOT NULL,
	candidato varchar PRIMARY KEY NOT NULL,
	conteo int DEFAULT 0 NOT NULL
);


CREATE TABLE IF NOT EXISTS conteoregion(
	region varchar PRIMARY KEY NOT NULL,
	conteo int DEFAULT 0 NOT NULL
);


CREATE TABLE IF NOT EXISTS conteovalido(
	esvalido bool PRIMARY KEY NOT NULL,
	conteo int DEFAULT 0 NOT NULL
);
