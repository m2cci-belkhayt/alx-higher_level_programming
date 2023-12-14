-- joining the cities withe its state that can be found in the database
SELECT cities.id, cities.name, states.name
FROM cities JOIN states
ON states.id = cities.state_id
ORDER BY cities.id ASC;