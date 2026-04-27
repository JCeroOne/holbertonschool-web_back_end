#!/usr/bin/env python3
"""Defines the list_all function."""


def list_all(mongo_collection):
    """Lists all the documents in a given collection."""
    if mongo_collection.find():
        return mongo_collection.find()

    return []
