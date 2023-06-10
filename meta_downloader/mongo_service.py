from pymongo import MongoClient


class MongoConnect:
    def __init__(self, url, db, coll):
        self.url = url
        self.db = db
        self.coll = coll
        self.connection()

    def connection(self):
        client = MongoClient(self.url)
        database = client[self.db]
        collection = database[self.coll]
        return collection
