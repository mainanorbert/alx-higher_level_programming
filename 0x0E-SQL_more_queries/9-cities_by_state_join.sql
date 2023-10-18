-- Listing cities in database
SELECT cities.id, cities.name, states.name as state_name FROM cities
JOIN states on Cities.state_id = states.id
ORDER BY cities.id ASC;
