--  script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT
	city, AVG(value) as avg_temp
FROM
	temperatures
where
	month = 7 or month = 8
group by city
order by avg_temp desc limit 3;
