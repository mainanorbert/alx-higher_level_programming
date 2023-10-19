-- listing all shows in database
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genre ON tv_show.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id
