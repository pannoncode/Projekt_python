from meta_downloader.downloader_service import MetaDataLoader
from meta_downloader.file_handler import FileHandler
from meta_downloader.config import movie_folder
from meta_downloader.mongo_service import MongoConnect

from meta_downloader.config import mongo_url, mongo_db, mongo_coll


def download_metadata():
    file = FileHandler()
    meta = MetaDataLoader()

    mongo = MongoConnect(mongo_url, mongo_db, mongo_coll)

    movies = file.get_files_path_from_folder(movie_folder)

    meta_data = sorted(item["title"]
                       for item in mongo.connection().find())

    # ha mindenhol egyezés van
    if movies == meta_data:
        print("egyezés")
        return

    # ha a mongodb tartalmaz olyan elemet, ami nincs benne a movies-ban
    for item in meta_data:
        print("törlés")
        if item not in movies:
            print(item)
            mongo.connection().delete_one({"title": item})
            poster_path = f"{FileHandler.posters}/{item}.jpg"
            FileHandler.remove_file(poster_path)

    # ha a movies -ban van olyan adat, ami nincs a mongo_db-ben
    for movie in [item for item in movies if item not in meta_data]:
        title = movie
        data = meta.download_metadata(title)
        download_path = meta.poster_path + data['poster_path']
        mongo.connection().insert_one(data)
        file.write_image(download_path, f"{file.posters}/{title}.jpg")


if __name__ == "__main__":
    download_metadata()
