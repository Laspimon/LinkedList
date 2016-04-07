#!/usr/bin/python
#-*-coding:utf8-*-
from __future__ import print_function

class Node(object):
    data = None
    next_ = None
    def __init__(self, num):
        self.data = num

class LinkedList(object):
    first = None

    def add_node(self, num):
        node = Node(num)
        if self.first is None:
            self.first = node
            return
        elif self.first.data > num:
            node.next_ = self.first
            self.first = node
            return
        pointer = self.first
        while True:
            if pointer.next_ is None:
                pointer.next_ = node
                return
            if pointer.next_.data > num:
                node.next_ = pointer.next_
                pointer.next_ = node
                return
            pointer = pointer.next_

    def walk(self):
        pointer = self.first
        while True:
            yield (pointer.data)
            if pointer.next_ is not None:
                pointer = pointer.next_
            else:
                break

if __name__ == '__main__':
    unittest.main()
