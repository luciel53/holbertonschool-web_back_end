#!/usr/bin/env python3
"""
    script that provides some stats about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient


client = MongoClient(host="localhost", port=27017)

db = client["logs"]
collection = db["nginx"]

# first line
numb_docs = collection.count_documents({})

# second line
method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for meth in method:
    numb_each_method = collection.count_documents({"method": method})
    print("{}: {}".format(method, numb_each_method))

get_count = collection.count_documents({"method": "GET", "path": "/status"})
print("{}: {}".format(method, get_count))
