file = open('movieList.txt')
movieTitle = file.read()
movies = movieTitle.splitlines()
print(movies[3])