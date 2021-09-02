CREATE DATABASE moviesdb;
\c moviesdb;

CREATE TABLE movies(
	id INT PRIMARY KEY,
	title CHAR(150));

CREATE TABLE crew(
	id INT PRIMARY KEY,
	name CHAR(60));

CREATE TABLE credit(
	id CHAR(30) PRIMARY KEY,
	crew INT,
	job_crew CHAR(60),
	movie INT,
	FOREIGN KEY (crew) REFERENCES crew (id),
	FOREIGN KEY (movie) REFERENCES movies (id));

CREATE TABLE casting(
	id CHAR(25) PRIMARY KEY,
	actor INT,
	movie INT,
	FOREIGN KEY (actor) REFERENCES crew (id),
	FOREIGN KEY (movie) REFERENCES movies (id));

CREATE TABLE genres(
	id INT PRIMARY KEY,
	name CHAR(25));

CREATE TABLE gen_movie(
	id SERIAL PRIMARY KEY,
	genres INT,
	movie INT,
	FOREIGN KEY (genres) REFERENCES genres (id),
	FOREIGN KEY (movie) REFERENCES movies (id));
	
CREATE TABLE votes(
	id SERIAL PRIMARY KEY,
	vote_count INT,
	vote_average DECIMAL,
	movie INT,
	FOREIGN KEY (movie) REFERENCES movies (id));

