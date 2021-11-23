-- script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0
SELECT distinct
	score, count(score) as `number`
FROM
	second_table
group by score
order by score DESC;
