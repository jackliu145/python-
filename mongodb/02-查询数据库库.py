from pymongo import MongoClient


client = MongoClient()

db = client.get_database('maomi')


print(db.maomi.find().count)