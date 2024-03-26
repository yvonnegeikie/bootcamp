# pip install IMDbPY - install this into terminal 
# https://www.geeksforgeeks.org/python-imdbpy-searching-a-movie/

import imdb
 
iMovie = imdb.IMDb()
 
search_movie = iMovie.search_movie('I am legend')
 
for movie in search_movie:
    print(movie)

print("\n")
character = iMovie.search_character("Thor")

for char in character:
    print(char)