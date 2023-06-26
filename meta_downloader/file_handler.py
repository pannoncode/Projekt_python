"""
This module handle file related task such as: 
write JSON files and get metadata from holders
"""
import os
import json


class FileHandler:
    root_folder = os.path.dirname(os.path.dirname(__file__))
    meta_data = os.path.join(root_folder, 'meta_data')
    posters = os.path.join(root_folder, 'posters')

    def __init__(self):
        self.create_folders()

    @staticmethod
    def get_files_path_from_folder(folder_path):
        temp = os.listdir(folder_path)
        files = []
        for item in temp:
            if item.split('.')[1] in ('mkv', 'json'):
                files.append(item.split('.')[0])
        return files

    def write_json(self, json_path, data):
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def create_folders(self):
        if not os.path.exists(self.meta_data):
            os.mkdir(self.meta_data)

        if not os.path.exists(self.posters):
            os.mkdir(self.posters)

    @staticmethod
    def write_image(download_path, file_name):
        from urllib.request import urlopen

        image = urlopen(download_path).read()

        with open(file_name, "wb") as poster:
            poster.write(image)

    @staticmethod
    def remove_file(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
        return True


if __name__ == '__main__':
    from downloader_service import MetaDataLoader

    f_path = r"/Users/tothgyorgy/Desktop/Python/Projekt_python/movies"
    test = FileHandler()

    meta = MetaDataLoader()

    movies = test.get_files_path_from_folder(f_path)
    title = movies[0]

    data = meta.download_metadata(title)
    download_path = meta.poster_path + data['poster_path']
    test.write_image(download_path, f"{test.posters}/{title}.jpg")
    test.write_json(f"{test.meta_data}/{title}.json", data)
