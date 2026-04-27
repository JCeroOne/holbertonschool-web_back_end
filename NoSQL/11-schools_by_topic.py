#!/usr/bin/env python3
"""Defines the schools_by_topic function."""


def schools_by_topic(mongo_collection, topic):
    """Lists all the schools with the specified topic."""
    res = []

    for school in mongo_collection.find():
        if "topics" in school and topic in school["topics"]:
            res.append(school)

    return res
