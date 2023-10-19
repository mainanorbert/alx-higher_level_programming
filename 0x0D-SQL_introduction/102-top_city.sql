-- selecting top 3 cities in terms of temperature
SELECT city, MAX(temperature) as max_temp
FROM city_temperatures
WHERE (MONTH(date) = 7 OR MONTH(date) = 8)
GROUP BY city
ORDER BY max_temp DESC
LIMIT 3;
