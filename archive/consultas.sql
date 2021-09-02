/*1- A)*/SELECT g.name, gm.genres, COUNT(gm.*)  FROM gen_movie gm JOIN genres g ON gm.genres=g.id GROUP BY gm.genres,g.name;

/*1- B)*/SELECT m.title, g.name FROM gen_movie gm JOIN genres g ON gm.genres=g.id JOIN movies m ON gm.movie=m.id ORDER BY gm.genres,gm.movie;

/*2- */SELECT name,k FROM (SELECT cr.name ,COUNT(c.*) AS k FROM casting c JOIN crew cr ON c.actor=cr.id GROUP BY c.actor,cr.name)AS t WHERE k=(SELECT MAX(k) FROM (SELECT COUNT(*) AS k FROM casting GROUP BY actor) l);

/*3- */SELECT title,k FROM (SELECT m.title ,COUNT(c.*) AS k FROM casting c JOIN movies m ON c.movie=m.id GROUP BY c.movie,m.title)AS t WHERE k=(SELECT MAX(k) FROM (SELECT COUNT(*) AS k FROM casting GROUP BY movie) l);

/*4- */SELECT crew,name,k FROM (SELECT c.crew,cr.name ,COUNT(c.*) AS k FROM credit c JOIN crew cr ON c.crew=cr.id where c.job_crew = 'Director' GROUP BY c.crew,cr.name)AS t WHERE k=(SELECT MAX(k) FROM (SELECT COUNT(*) AS k FROM credit where job_crew = 'Director' GROUP BY crew) l);

/*5- */SELECT m.title, ca.actor, ca.movie FROM casting ca JOIN credit c ON c.crew=ca.actor AND c.movie= ca.movie JOIN movies m ON c.movie=m.id WHERE c.job_crew = 'Director';

/*6- */SELECT m.title, v.movie,v.vote_count FROM votes v JOIN movies m ON v.movie=m.id WHERE v.vote_count = (SELECT MAX(vote_count) FROM votes);

/*7- */SELECT m.title, v.movie,v.vote_average FROM votes v JOIN movies m ON v.movie=m.id WHERE v.vote_average = (SELECT MAX(vote_average) FROM votes);
