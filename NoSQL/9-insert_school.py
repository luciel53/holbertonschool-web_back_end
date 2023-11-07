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
    new_doc = kwargs
    mongo_collection.insert(new_doc)
    return id(new_doc)
