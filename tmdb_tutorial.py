import tmdbsimple as tmdb
from urllib.request import urlopen

tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

search = tmdb.Search()

response = search.movie(query='Alien')['results'][0]

print(response)

image = urlopen(
    "https://image.tmdb.org/t/p/original/AmR3JG1VQVxU8TfAvljUhfSFUOx.jpg").read()

with open('test.jpg', "wb") as poster:
    poster.write(image)
