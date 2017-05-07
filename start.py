#!/usr/bin/python
import data_movies
import fresh_tomatoes

data_movies = data_movies.DataMovies()

fresh_tomatoes.open_movies_page(data_movies.data_movies_list)
