from pymongo import MongoClient
# import certifi

# ca = certifi.where()
cluster = MongoClient("mongodb+srv://z1k01ff:1234@cluster0.j31cyfd.mongodb.net/?retryWrites=true&w=majority")
db = cluster["TEST_DB"]
collection = db["TEST_Collection"]
collection.insert_one({"_id": 1, "name": "Nazar"})

