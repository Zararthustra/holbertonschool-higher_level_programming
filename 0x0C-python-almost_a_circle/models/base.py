#!/usr/bin/python3
"""
base class module
"""
import json


class Base:
    """
    init class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor
            args:
                id (int): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """
        returns a JSON string representation of
        json_string list of dict
        """
        if json_string:
            if type(json_string) is str:
                return json.loads(json_string)
        else:
            return "[]"

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries:
            if type(list_dictionaries) is list:
                return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON str list_objs to a file
        """
        dic_list = []
        filename = "{}.json".format(cls.__name__)

        if list_objs is None:
            list_objs = []
        for o in list_objs:
            dic_list.append(o.to_dictionary())
        with open(filename, mode="w") as f:
            f.write(cls.to_json_string(dic_list))
