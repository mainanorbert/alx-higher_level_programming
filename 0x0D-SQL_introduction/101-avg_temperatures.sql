-- importing and displaying temperature in fehrenheit
SELECT city, AVG((temperature - 32) * 5/9) as avg_temp
FROM city_temperatures
GROUP BY city
ORDER BY avg_temp DESC
