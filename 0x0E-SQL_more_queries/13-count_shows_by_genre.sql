-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- shows linked to each.
SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
    JOIN `tv_show_genres` AS t
    ON g.`id` = s.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;