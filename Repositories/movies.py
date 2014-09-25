
movie_titles = ["Amelie", "Eternal Sunshine of the Spotless Mind", "Flight of the Navigator", "The Grand Budapest Hotel", "Requiem for a Dream"]
parental_rating = ["R", "R", "PG", "R", "R"]
bechdel_rating = [3, 2, 1, 1, 3]
imdb_rating = [8.5, 8.4, 6.9, 8.4, 8.4]
genre = ["Comedy / Romance", "Drama / Romance / Sci-Fi", "Adventure / Family / Sci-Fi", "Comedy", "Drama"]

for movie_titles, parental_rating, bechdel_rating, imdb_rating, genre in zip(movie_titles, parental_rating, bechdel_rating, imdb_rating, genre):
        print "{0}, {1}, {2}, {3}, {4}".format(movie_titles, parental_rating, bechdel_rating, imdb_rating, genre)
