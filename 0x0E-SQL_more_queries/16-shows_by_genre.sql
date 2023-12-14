-- Lists all shows and genres linked to the show from the
-- database hbtn_0d_tvshows.
-- Records are ordered by ascending show title and genre name.
SELECT titileshow.`title`, genreshow.`name`
  FROM `tv_shows` AS titileshow
       LEFT JOIN `tv_show_genres` AS show
       ON titileshow.`id` = show.`show_id`
       LEFT JOIN `tv_genres` AS genreshow
       ON show.`genre_id` = genreshow.`id`
 ORDER BY titileshow.`title`, genreshow.`name`;