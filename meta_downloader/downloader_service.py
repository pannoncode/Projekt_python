from urllib.request import urlopen

import tmdbsimple as tmdb


class MetaDataLoader:
    tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'
    poster_path = "https://image.tmdb.org/t/p/original"

    def __init__(self):
        # ez nem a legszebb megoldás
        # SOLID principles <- ezt az elvet kéne követni  Dependenxy injection-nak ellent mond
        self.search = tmdb.Search()

    def download_metadata(self, title):
        meta_data = self.search.movie(query=title)['results']

        if not meta_data:
            return False

        return meta_data[0]


if __name__ == "__main__":
    test = MetaDataLoader()
