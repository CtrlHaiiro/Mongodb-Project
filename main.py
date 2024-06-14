from pymongo import MongoClient

try:
    client = MongoClient('mongodb+srv://mongodb-ele.xku5epx.mongodb.net/')
    db = client.get_database("Concerti")
except Exception:
    print(Exception)

print(db.name)
