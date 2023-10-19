-- Listing cities in database
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states on cities.state_id = states.id
ORDER BY cities.id ASC;
