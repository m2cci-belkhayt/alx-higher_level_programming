-- Lists all comedy shows in the database hbtn_0d_tvshows.
-- Records are ordered by descending show title.
SELECT showtitle.`title`
  FROM `tv_shows` AS showtitle
       INNER JOIN `tv_show_genres` AS show
       ON showtitle.`id` = show.`show_id`
       INNER JOIN `tv_genres` AS gen
       ON gen.`id` = s.`genre_id`
       WHERE gen.`name` = "Comedy"
 ORDER BY showtitle.`title`;