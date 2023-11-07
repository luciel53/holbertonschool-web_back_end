#!/usr/bin/env python3
"""
    Python function that lists all documents in a collection:

    Prototype: def list_all(mongo_collection):
    Return an empty list if no document in the collection
    mongo_collection will be the pymongo collection object
"""


def list_all(mongo_collection):
    """ function to list all documents in the collection """
    docs_in_collection = list(mongo_collection.find())
    if docs_in_collection.count() == 0:
        return []
    return docs_in_collection
