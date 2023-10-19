-- displaying mac temp for each state
SELECT name, MAX(temperature) as max_temp FROM states
GROUP BY name
ORDER BY name
