from meta_downloader.downloader_service import MetaDataLoader
from meta_downloader.file_handler import FileHandler
from meta_downloader.config import movie_folder, url
from meta_downloader.mongo_service_2 import MongoService


def download_metadata():
    mongo = MongoService()
    file = FileHandler()
    meta = MetaDataLoader()

    movies = file.get_files_path_from_folder(movie_folder)

    movies_lower = sorted([item.lower() for item in movies])

    meta_data = sorted([item['title'].lower()
                       for item in mongo.get_all_meta()])

    if movies_lower == meta_data:
        return

    for item in meta_data:
        if item not in movies_lower:
            mongo.delete_movie(item)
            poster_path = f"{FileHandler.posters}/{item}.jpg"
            FileHandler.remove_file(poster_path)

    for movie in [item for item in movies_lower if item not in meta_data]:
        title = movie
        data = meta.download_metadata(title)
        download_path = meta.poster_path + data['poster_path']

        data["my_poster_path"] = f"{file.posters}/{title}.jpg"

        mongo.insert_movie(data)

        file.write_image(download_path, f"{file.posters}/{title}.jpg")


if __name__ == '__main__':
    download_metadata()
