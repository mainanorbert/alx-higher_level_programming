-- listing all shows in database
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genre ON tv_show.genre.id = tv_show.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id
