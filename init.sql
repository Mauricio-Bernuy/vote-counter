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

list( myBigList[i] for i in [0,1,2] )

INSERT INTO votos VALUES('regiontest', 'provinciatest', 'ciudadtest', 123456, 'Larry K.', TRUE);

(region != 'Lima' OR region != 'La Libertad' OR region != 'Arequipa')



SELECT 1 FROM conteovotos WHERE candidato={candidato};
SELECT 1 FROM conteoregion WHERE region={region};
SELECT 1 FROM conteovalido WHERE esvalido={esvalido};


if true: 

UPDATE conteovotos set conteo = conteo + 1 WHERE (region = {region} AND candidato = {candidato});
UPDATE conteoregion set conteo = conteo + 1 WHERE (region = {region});
UPDATE conteovalido set conteo = conteo + 1 WHERE (esvalido = {esvalido});

else:

INSERT INTO conteovotos VALUES({region},{candidato},0);
INSERT INTO conteoregion VALUES({region},0);
INSERT INTO conteovalido VALUES({esvalido},0);


db_conn.invalidate()
db_conn.close()
pool.dispose()

SELECT sum(numbackends) FROM pg_stat_database;
select * from conteoregion;
select count(*)  from votos  where esvalido = TRUE;
delete from votos; delete from conteoregion;
select count(*) from votos where consumed = TRUE;
delete from votos; delete from conteoregion; delete from conteovotos; delete from conteovalido;

INSERT INTO the_table (id, column_1, column_2) 
VALUES (1, 'A', 'X'), (2, 'B', 'Y'), (3, 'C', 'Z')
ON CONFLICT (id) DO UPDATE 
  SET column_1 = excluded.column_1, 
      column_2 = excluded.column_2;

INSERT INTO conteoregion VALUES({region},0)
ON CONFLICT (region) DO UPDATE 
conteoregion SET conteo = conteo + 1 WHERE (region = {region});


REMINDER: CON 10 funciona! (se vuelve lento dsps de cierto punto tho)

maybe small sleep en el producer?

maybe mantener la instance en vez del pool?


podria hacerse un batch de queries? apendear a lista hasta que tenga cierto tamaño y guardada de manera global.
de ahi ejecutarlo todo en un execute()

working ish for now!


TODO: API que devuelva las tablas. para la tabla de conteovotos pedir un /api/<Region> y devolver en base a eso.
volverlos json