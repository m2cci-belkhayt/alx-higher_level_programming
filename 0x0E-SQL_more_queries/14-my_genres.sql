-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT mygenre.`name`
  FROM (`tv_genres` AS mygenre
       INNER JOIN `tv_show_genres` AS showtv
       ON mygenre.`id` = showtv.`genre_id`)
       INNER JOIN (`tv_shows` AS t
       ON t.`id` = mygenre.`show_id`
       WHERE t.`title` = "Dexter")
 ORDER BY mygenre.`name`;