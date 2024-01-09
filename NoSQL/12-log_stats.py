#!/usr/bin/env python3
'''
Module to print status of logs and 
most Methods
'''


from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    logs_collection = client.logs.nginx

    print(f"{logs_collection.count({})} logs")
    print(f"\tmethod GET: {logs_collection.count({'method': 'GET'})}")
    print(f"\tmethod POST: {logs_collection.count({'method': 'POST'})}")
    print(f"\tmethod PUT: {logs_collection.count({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {logs_collection.count({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {logs_collection.count({'method': 'DELETE'})}")
    print(f"{logs_collection.count({'path': '/status'})} status check")