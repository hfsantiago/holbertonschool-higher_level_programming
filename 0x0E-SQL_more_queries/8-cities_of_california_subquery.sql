-- Lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT cities.id, cities.name FROM cities, states WHERE `states`.`id` = state_id and states.name = 'California';

