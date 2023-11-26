# coding: UTF-8

import copy

class Packet:
    
    def __init__(self, counter):
        self.__counter = counter
        self.__route = []
        
    def getCounter(self):
        return self.__counter
    
    def getRoute(self):
        return self.__route
        
    def decrement(self):
        self.__counter = self.__counter - 1
        
    def clone(self):
        return copy.deepcopy(self)
    
    def tostring(self):
        return 'Packet transport route is : ' + str(self.__route)