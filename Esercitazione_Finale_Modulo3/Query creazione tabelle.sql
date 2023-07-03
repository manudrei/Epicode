CREATE DATABASE video_games;




CREATE TABLE videogames.dbo.platform (
	id INT PRIMARY KEY,
	platform_name VARCHAR(50)
);

CREATE TABLE videogames.dbo.genre (
	id INT PRIMARY KEY,
	genre_name VARCHAR(50)
);

CREATE TABLE videogames.dbo.publisher (
	id INT PRIMARY KEY,
	publisher_name VARCHAR(100)
);

CREATE TABLE videogames.dbo.region (
	id INT PRIMARY KEY,
	region_name VARCHAR(50)
);

INSERT INTO videogames.dbo.region VALUES 
(1,'North America'),
(2,'Europe'),
(3,'Japan'),
(4,'Other');

CREATE TABLE videogames.dbo.game (
	id INT PRIMARY KEY,
	genre_id INT,
	game_name VARCHAR(200),
	CONSTRAINT fk_gm_gen FOREIGN KEY (genre_id) REFERENCES videogames.dbo.genre(id)
);

CREATE TABLE videogames.dbo.game_publisher (
	id INT PRIMARY KEY,
	game_id INT,
	publisher_id INT,
	CONSTRAINT fk_gpu_gam FOREIGN KEY (game_id) REFERENCES videogames.dbo.game(id),
	CONSTRAINT fk_gpu_pub FOREIGN KEY (publisher_id) REFERENCES videogames.dbo.publisher(id)
);

CREATE TABLE videogames.dbo.game_platform (
	id INT PRIMARY KEY,
	game_publisher_id INT,
	platform_id INT,
	release_year INT,
	CONSTRAINT fk_gpl_gp FOREIGN KEY (game_publisher_id) REFERENCES videogames.dbo.game_publisher(id),
	CONSTRAINT fk_gpl_pla FOREIGN KEY (platform_id) REFERENCES videogames.dbo.platform(id)
);

CREATE TABLE videogames.dbo.region_sales (
	region_id INT,
	game_platform_id INT,
	num_sales DECIMAL(5, 2),
    CONSTRAINT fk_rs_gp FOREIGN KEY (game_platform_id) REFERENCES videogames.dbo.game_platform(id),
	CONSTRAINT fk_rs_reg FOREIGN KEY (region_id) REFERENCES videogames.dbo.region(id)
);
 /* Per l'importazione dei dati ho usato il trucchetto che ci hai insegnato a lezione tramite Excel, ho trovato un dataset csv da dove ho estrapolato e importato su excel ed infine importato su SQL con il tuo trucchetto. La tabella region_sales i dati num_sales sono totalmente creati da me tramite excel */