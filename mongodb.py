
from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017")

    db = client["Userdata"]

    users = db["Userinfo"]  

except Exception as e:
    print(e)
    users=None

def get_collection():
        if users is None:
             raise Exception("MongoDB connection failed")
        return users









