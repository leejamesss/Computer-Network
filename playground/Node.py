# coding: UTF-8

import Packet

class Node:

    def __init__(self, name):
        self.__name = name
        self.__isEnd = False
        self.__relativeNodes = []

    def link(self, nodes):
        for relativeNode in nodes:
            self.__relativeNodes.append(relativeNode)
            relativeNode.getRelativeNodes().append(self)

    def getRelativeNodes(self):
        return self.__relativeNodes

    def accept(self, packet):
        packet.getRoute().append(self.__name)
        
        if (self.__isEnd):
            print 'Transport Success : ' + packet.tostring()
        elif (0 == packet.getCounter()):
            print 'Transport Fail(End) : ' + packet.tostring()
        else :
            packet.decrement()
            
            isAvailableNodeExist = False
            for nextNode in self.__relativeNodes:
                if (nextNode.getName() not in packet.getRoute()):
                    isAvailableNodeExist = True
                    nextNode.accept(packet.clone())
            
            if (not isAvailableNodeExist):
                print 'Transport Fail : ' + packet.tostring()
    
    def setEnd(self, isEnd) :
        self.__isEnd = isEnd
        
    def getName(self):
        return self.__name
    
