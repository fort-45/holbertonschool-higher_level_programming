#!/usr/bin/python3
'''
ha ha ha document
'''


class Rectangle:
    '''
    whooooo houuuu
    '''
    def __init__(self, width, height):
        '''
        Initializes a new Rectangle instance
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        salam salam
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        setter fir width
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        salam salam
        '''
        return self.__height

    @width.setter
    def height(self, value):
        '''
        setter fir width
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
