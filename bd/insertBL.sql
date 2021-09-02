\COPY movies(id ,title) FROM 'movies.csv' DELIMITER ',' CSV HEADER;

\COPY genres(id ,name) FROM 'genres.csv' DELIMITER ',' CSV HEADER;

\COPY crew(id ,name) FROM 'crew.csv' DELIMITER ',' CSV HEADER;

\COPY gen_movie(genres,movie) FROM 'gen_mov.csv' DELIMITER ',' CSV HEADER;

\COPY credit(id ,crew,job_crew,movie) FROM 'credito.csv' DELIMITER ',' CSV HEADER;

\COPY casting(id ,actor,movie) FROM 'casting.csv' DELIMITER ',' CSV HEADER;

\COPY votes(movie, vote_average,vote_count) FROM 'votes.csv' DELIMITER ',' CSV HEADER;
