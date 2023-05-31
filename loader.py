from meta_downloader.downloader_service import MetaDataLoader
from meta_downloader.file_handler import FileHandler
from meta_downloader.config import movie_folder


def download_metadata():
    file = FileHandler()
    meta = MetaDataLoader()

    movies = file.get_files_path_from_folder(movie_folder)

    for movie in movies:
        title = movie
        data = meta.download_metadata(title)
        download_path = meta.poster_path + data['poster_path']
        file.write_image(download_path, f"{file.posters}/{title}.jpg")
        file.write_json(f"{file.meta_data}/{title}.json", data)


if __name__ == "__main__":
    download_metadata()
