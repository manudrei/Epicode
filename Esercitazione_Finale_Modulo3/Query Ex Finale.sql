
SELECT 
		g.game_name AS Videogame, 
		gn.genre_name AS Genre, 
		pu.publisher_name AS Publisher, 
		p.platform_name AS Platform, 
		gp.release_year AS YEAR 
FROM game g
INNER JOIN genre gn
ON g.genre_id=gn.id 
INNER JOIN game_publisher gpu
ON gpu.game_id = g.id
INNER JOIN publisher pu
ON gpu.publisher_id = pu.id
INNER JOIN game_platform gp
ON gp.game_publisher_id = gpu.id
INNER JOIN platform p
ON gp.platform_id = p.id
ORDER BY g.game_name;  /*Tramite delle join ho ottenuto una tabella con le colonne del videogioco, il genere, il produttore, la piattaforma e l'anno d'uscita */

SELECT 
		COUNT(gp.release_year) as GameByYear, 
		gp.release_year as YEAR 
FROM game g
INNER JOIN genre gn
ON g.genre_id=gn.id 
INNER JOIN game_publisher gpu
ON gpu.game_id = g.id
INNER JOIN publisher pu
ON gpu.publisher_id = pu.id
INNER JOIN game_platform gp
ON gp.game_publisher_id = gpu.id
INNER JOIN platform p
ON gp.platform_id = p.id
GROUP BY release_year
ORDER BY release_year /* Queste join mostrano quanti giochi sono usciti in ogni singolo anno */


SELECT 
	p.platform_name as Platform , 
	sum(num_sales) as TotalSales
FROM game g
INNER JOIN genre gn
ON g.genre_id=gn.id 
INNER JOIN game_publisher gpu
ON gpu.game_id = g.id
INNER JOIN publisher pu
ON gpu.publisher_id = pu.id
INNER JOIN game_platform gp
ON gp.game_publisher_id = gpu.id
INNER JOIN platform p
ON gp.platform_id = p.id
INNER JOIN region_sales rs
ON rs.game_platform_id = gp.id
INNER JOIN region r
ON r.id = rs.region_id
GROUP BY p.platform_name
ORDER BY TotalSales DESC	/*Questa tabella mostra le piattaforme più proficue */




