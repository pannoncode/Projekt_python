from meta_downloader.downloader_service import MetaDataLoader
from meta_downloader.file_handler import FileHandler
from meta_downloader.config import movie_folder

"""
Kezeljük le azt az esetet,
amikor törlök egy filmet, akkor mi legyen a már letöltött metaadatokkat
"""


def download_metadata():
    file = FileHandler()
    meta = MetaDataLoader()

    movies = file.get_files_path_from_folder(movie_folder)
    meta_json = file.get_files_path_from_folder(file.meta_data)

    """
    ha meta_json == movies -> nem kell csinálni semmit

    ha a meta_json tartalmaz ilyan elemet, 
    ami nincs benne a movies-ban -> törlöm ezt az adatot a meta_data és posters folderekből

    ha a movies -ban van olyan adat, ami nincs a meta_json-ben -> letölteni a metaadatot
    """

    if movie == meta_json:
        return

    for item in meta_json:
        if item not in movies:
            # ide kell a törlés
            json_path = f"{FileHandler.meta_data}/{item}.json"
            poster_path = f"{FileHandler.posters}/{item}.jpg"

            FileHandler.remove_file(json_path)
            FileHandler.remove_file(poster_path)
            pass

    # temp = []
    # for item in movies:
    #     if item not in meta_json:
    #         temp.append(item)
    #         # itt kellene letölteni
    # list comprehension lett belőle a for ciklusban

    for movie in [item for item in movies if item not in meta_json]:
        title = movie
        data = meta.download_metadata(title)
        download_path = meta.poster_path + data['poster_path']
        file.write_image(download_path, f"{file.posters}/{title}.jpg")
        file.write_json(f"{file.meta_data}/{title}.json", data)


if __name__ == "__main__":
    download_metadata()
