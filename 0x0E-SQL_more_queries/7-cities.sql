-- creating tables for cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	PRIMARY KEY(id),
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	state_id INT NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
	);
