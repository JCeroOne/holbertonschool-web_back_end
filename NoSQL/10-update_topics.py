#!/usr/bin/env python3
"""Defines the update_topics function."""


def update_topics(mongo_collection, name, topics):
    """Updates the collection with the given parameters."""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
