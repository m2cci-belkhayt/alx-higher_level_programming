-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Records are sorted by ascending tv_shows.title and tv_show_genres.gen
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
  JOIN `tv_show_genres` AS g
  ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;