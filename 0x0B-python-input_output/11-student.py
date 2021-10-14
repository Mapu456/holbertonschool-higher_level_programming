#!/usr/bin/python3
'''
    Module that defines a student class
'''


class Student:
    '''
        Defines a student class
    '''

    def __init__(self, first_name, last_name, age):
        '''
        Defines a student class
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Defines a student class
        '''
        if attrs is None:
            return self.__dict__
        new_dict = dict()
        for i in self.__dict__:
            if i in attrs:
                new_dict[i] = self.__dict__[i]
        return new_dict

    def reload_from_json(self, json):
        for key in json:
            for key_self in self.__dict__:
                if key == key_self:
                    self.__dict__[key_self] = json[key]
