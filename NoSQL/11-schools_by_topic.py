#!/usr/bin/env python3
'''
NoSQL
'''


def schools_by_topic(mongo_collection, topic):


    '''
    function that lists all documents in a collection
    '''
    return mongo_collection.find({"topics": topic})