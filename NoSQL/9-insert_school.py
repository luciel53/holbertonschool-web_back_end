#!/usr/bin/env python3
"""
    Python function that inserts a new document in a collection
    based on kwargs:

    Prototype: def insert_school(mongo_collection, **kwargs):
    mongo_collection will be the pymongo collection object
    Returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """ function to insert a new document in a collection """
    new_doc = mongo_collection.insert(kwargs)
    return new_doc
