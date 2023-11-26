# coding: UTF-8

import Node
import Packet

if __name__ == '__main__':
    node1 = Node.Node('1')
    node2 = Node.Node('2')
    node3 = Node.Node('3')
    node4 = Node.Node('4')
    node5 = Node.Node('5')
    node6 = Node.Node('6')
    node7 = Node.Node('7')
    node8 = Node.Node('8')
    node9 = Node.Node('9')
    node10 = Node.Node('10')

    node1.link([node2, node3, node6])
    node2.link([node3, node10])
    node4.link([node6])
    node5.link([node6])
    node6.link([node8])
    node7.link([node8])
    node8.link([node9, node10])
    
    node7.setEnd(True)
    node1.accept(Packet.Packet(3))

