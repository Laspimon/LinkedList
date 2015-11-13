#!/usr/bin/python
#-*-coding:utf8-*-
from __future__ import print_function
import unittest

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

class TestAddNote(unittest.TestCase):

    def test_add_one(self):
        ll = LinkedList()
        for i in [1]: ll.add_node(i)
        self.assertEqual([1], [x for x in ll.walk()])

    def test_add_one_two_one(self):
        ll = LinkedList()
        for i in [2, 1]: ll.add_node(i)
        self.assertEqual([1, 2], [x for x in ll.walk()])

    def test_add_range10(self):
        ll = LinkedList()
        for i in range(9,0,-2) + range(0,10,2): ll.add_node(i)
        self.assertEqual(range(10), [x for x in ll.walk()])

    def test_add_negative(self):
        ll = LinkedList()
        for i in range(5) + [-10, -1, 0, 1]: ll.add_node(i)
        self.assertEqual([-10, -1, 0, 0, 1, 1, 2, 3, 4], [x for x in ll.walk()])

    def test_float(self):
        ll = LinkedList()
        for i in [1, 1.0, 1.1, 0.9]: ll.add_node(i)
        self.assertEqual([0.9, 1, 1.0, 1.1], [x for x in ll.walk()])

if __name__ == '__main__':
    unittest.main()
