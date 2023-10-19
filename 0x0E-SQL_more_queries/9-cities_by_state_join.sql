-- Listing cities in database
SELECT cities.id, cities.name, states.name AS state_name FROM cities
JOIN states on cities.state_id = states.id
ORDER BY cities.id ASC;
