#!/usr/bin/env python3
"""Defines the insert_school function."""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into the given collection."""

    mongo_collection.insert_one(kwargs)

    return mongo_collection.find_one(kwargs)["_id"]
