from pymongo import MongoClient
from power import Power
import psutil
import time
import os
import pymongo.errors

cs = "mongodb+srv://mongoadmin:[password]@cluster0.kufmp0l.mongodb.net/?retryWrites=true&w=majority"
# cs = os.environ.get('connectionString')

client = MongoClient(cs)


db = client["powstat"]
col = db["stat"]

print(col.find_one())
#print(col.count_documents({}))

"""
while True:

  
    try:
        if col.count_documents({}) >= 10000:
            oldest_document = col.find_one({}, sort=[("_id", 1)])  # Find the oldest document
            col.delete_one({"_id": oldest_document["_id"]})  # Delete the oldest document

        power = Power(psutil.cpu_percent(), psutil.virtual_memory()[1], psutil.virtual_memory()[4], time.localtime())
        col.insert_one(power.to_dict())  # Insert the new document
        time.sleep(1)

    except pymongo.errors.ServerSelectionTimeoutError:
        print("Connection to MongoDB server lost. Retrying...")
        """