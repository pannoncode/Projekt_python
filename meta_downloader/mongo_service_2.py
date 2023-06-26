from pymongo import MongoClient


class MongoService:
    db_uri = "mongodb://localhost:27017"

    def __init__(self):
        self.client = MongoClient(self.db_uri)
        self.database = self.client['movie_meta']
        self.collection = self.database['meta']

    def insert_movie(self, data):
        return self.collection.insert_one(data)

    def get_all_meta(self):
        return self.collection.find({"title": {"$exists": True}}, {'title': 1, '_id': 0})

    def delete_movie(self, title):
        return self.collection.delete_one({'$regex': title, '$options': 'i'})


if __name__ == '__main__':
    mongo = MongoService()

    mongo.collection.insert_one({'test': 'test value', 'title': 'Prey'})
    mongo.collection.insert_one({'test': 'test value', 'title': 'Alien'})
    result = mongo.get_all_meta()

    print([item for item in result])
