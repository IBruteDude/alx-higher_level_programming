#!/usr/bin/python3
"""Module for defining the Base class"""
from json import dumps, loads
from csv import reader, writer


class Base:
    """The Base class for all the modeled classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialises the id of the instance

        Args:
            id (int, optional): the id for the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """serialises a list of dict objects into the json format

        Args:
            list_dictionaries (list[dict]): the list of dicts

        Returns:
            str: the serialised json string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a list of instances of an inheriting class to a json file

        Args:
            list_objs (list[Base]): list of instances
        """
        with open(cls.__name__ + '.json', 'w') as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            list_objs = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """deserialises a string of json data into python objects

        Args:
            json_string (str): the input json encoded string

        Returns:
            Any: the decoded objects
        """
        if json_string is None or len(json_string) == 0:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance of a specific inheriting class with

        Returns:
            (Rectangle | square): the created instance
        """
        ctr_args = [1] * len(dictionary)
        instance = cls(*ctr_args)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """loads and instantiates a json file as a specified class"""
        try:
            file = open(cls.__name__ + '.json', 'r')
        except Exception:
            return []
        dict_list = Base.from_json_string(file.read())
        file.close()
        return [cls.create(**dict) for dict in dict_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open(cls.__name__ + ".csv", mode='w') as file:
            if cls.__name__ == 'Rectangle':
                file.write("id,width,height,x,y\n")
                for obj in list_objs:
                    file.write(
                        f"{obj.id},{obj.width},{obj.height},{obj.x},{obj.y}\n"
                    )
            elif cls.__name__ == 'Square':
                file.write("id,size,x,y\n")
                for obj in list_objs:
                    file.write(
                        f"{obj.id},{obj.size},{obj.x},{obj.y}\n"
                    )
            else:
                keys = list(cls.__dict__.keys())
                file.write(str(keys)[1:-1] + '\n')
                for obj in list_objs:
                    file.write(
                        ','.join([vars(obj)[key] for key in keys]) + '\n'
                    )

    @classmethod
    def load_from_file_csv(cls):
        with open(cls.__name__ + ".csv", mode='r') as file:
            lines = file.readlines()
            keys = lines[0][:-1].split(',')
            del lines[0]
            # returned_list = []
            # for line in lines:
            #     line = line[:-1]
            #     str_values_list = line.split(',')
            #     extracted_integers = map(lambda x: int(x), str_values_list)
            #     attr_list = list(extracted_integers)
            #     tuple_list = zip(keys, attr_list)
            #     dict_obj = dict(tuple_list)
            #     obj = cls.create(**dict_obj)
            #     returned_list.append(obj)
            return [
                cls.create(**dict(
                    zip(keys, list(
                        map(lambda x: int(x), line[:-1].split(','))
                    ))
                ))
                for line in lines
            ]  # returned_list
