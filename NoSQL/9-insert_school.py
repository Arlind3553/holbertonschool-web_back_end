#!/usr/bin/env python3
'''
NoSQL
'''


def insert_school(mongo_collection, **kwargs):
    '''
    function that lists all documents in a collection
    '''
    cd = mongo_collection.insert_one(kwargs).inserted_id
    return cd