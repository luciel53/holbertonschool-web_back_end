#!/usr/bin/env python3
"""
    Write a Python function that returns the list of school having a specific
    topic:

    Prototype: def schools_by_topic(mongo_collection, topic):
    mongo_collection will be the pymongo collection object
    topic (string) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """ function that returns a list of school with specific topic """
    to_return = mongo_collection.find({"topics": topic})
    return to_return
