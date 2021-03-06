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

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance from a dict
            args:
                dictionary (dict): attributes already set
        """
        if cls.__name__ == "Square":
            dummy_instance = cls(1, 0, 0)
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1, 0, 0)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @staticmethod
    def from_json_string(json_string):
        """
        returns a JSON string representation of
        json_string list of dict
            args:
                json_string (str): [dict]
        """
        if json_string is None and type(json_string) is not str:
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
            args:
                list_dictionaries (list): list of dict to translate
        """
        if list_dictionaries:
            if type(list_dictionaries) is list:
                return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances from a file
        """
        filename = cls.__name__ + ".json"
        inst_list = []

        try:
            with open(filename, mode="r") as f:
                for dic in cls.from_json_string(f.read()):
                    inst_list.append(cls.create(**dic))
        except:
            pass
        return inst_list

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON str list_objs to a file
            args:
                list_objs (json str): JSON str
        """
        dic_list = []
        filename = "{}.json".format(cls.__name__)

        if list_objs is None:
            list_objs = []
        for o in list_objs:
            dic_list.append(o.to_dictionary())
        with open(filename, mode="w") as f:
            f.write(cls.to_json_string(dic_list))
