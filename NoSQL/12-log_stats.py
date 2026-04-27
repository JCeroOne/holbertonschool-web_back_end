#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


if name == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx = client.logs.nginx

    print("{} logs".format(nginx.count()))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for m in methods:
        print(f"\tmethod {}: {}".format(
            m,
            nginx.find({"method": m}).count()
        ))

    print("{} status check".format(
        nginx.find({
            "method": "GET",
            "path": "/status"
        }).count()
    ))
