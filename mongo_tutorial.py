from pymongo import MongoClient

# kapcsolat a MongoDB-hez
client = MongoClient("mongodb://localhost:27017")
# kapcsolat az adatbázishoz
database = client['test']
# kapcsolat a collectionhöz
coll = database['my_coll']

# test_data = {
#     "salary": 10_000,
#     "position": "developer"
# }

# coll.insert_one(test_data)

# coll.delete_one({"position": "developer"})
# coll.delete_many({"position": "developer"})

test_data = [{"salary": 1000 + item * 10} for item in range(100)]

# coll.insert_many(test_data)

filter = {"salary": {"$lt": 1500}}
# coll.update_many(filter, {"$set": {"name": "Ricsi"}})

# data = coll.find_one(filter)
# print(data)
# for item in coll.find(filter, {'_id': 0, "name": 1}):
#     print(item)
