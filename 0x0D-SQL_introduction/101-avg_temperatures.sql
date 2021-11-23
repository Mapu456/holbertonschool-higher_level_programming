-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT
	city, AVG(value) as avg_temp
FROM
	temperatures
group by city
order by avg_temp DESC;
