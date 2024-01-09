#!/usr/bin/env python3
'''
NoSQL
'''


def update_topics(mongo_collection, name, topics):

    '''
    function that lists all documents in a collection
    '''
    myquery = { "name": name }
    newvalues = { "$set": { "topics": topics } }

    mongo_collection.update_one(myquery, newvalues)