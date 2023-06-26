from meta_downloader.downloader_service import MetaDataLoader
from meta_downloader.file_handler import FileHandler
from meta_downloader.config import movie_folder, url
from meta_downloader.meta_tables import (movie_meta,
                                         movie_genre,
                                         insert_movie_meta,
                                         insert_movie_genre,
                                         select_meta,
                                         delete_meta,
                                         delete_genre)
from meta_downloader.postgres_service import DatabaseHandler
"""
Kezeljük le azt az esetet,
amikor törlök 1 filmet, akkor mi legyen a már letöltött metaadatokkal
"""


def download_metadata():
    sql = DatabaseHandler(url)

    sql.run_query(movie_meta)
    sql.run_query(movie_genre)

    file = FileHandler()
    meta = MetaDataLoader()

    movies = file.get_files_path_from_folder(movie_folder)

    movies_lower = sorted([item.lower() for item in movies])

    meta_data = sorted([item[0].lower()
                       for item in sql.run_query(select_meta, True)])

    if movies_lower == meta_data:
        return

    for item in meta_data:
        if item not in movies_lower:
            sql.run_query(delete_genre.format(title=item))
            sql.run_query(delete_meta.format(title=item))
            poster_path = f"{FileHandler.posters}/{item}.jpg"
            FileHandler.remove_file(poster_path)

    for movie in [item for item in movies_lower if item not in meta_data]:
        title = movie
        data = meta.download_metadata(title)
        download_path = meta.poster_path + data['poster_path']
        genre_ids = data.pop('genre_ids')

        final_genre = []

        for item in genre_ids:
            final_genre.append({"movie_id": data['id'], "genre_id": item})

        data["my_poster_path"] = f"{file.posters}/{title}.jpg"
        sql.insert_data(insert_movie_meta, data)
        sql.insert_data(insert_movie_genre, final_genre)

        file.write_image(download_path, f"{file.posters}/{title}.jpg")


if __name__ == '__main__':
    download_metadata()
