from linked_list import LinkedList, Node

from nose.tools import assert_equals

class TestAddNote(object):
    def test_add_one(self):
        ll = LinkedList()
        for i in [1]: ll.add_node(i)
        assert_equals([1], [x for x in ll.walk()])

    def test_add_one_two_one(self):
        ll = LinkedList()
        for i in [2, 1]: ll.add_node(i)
        assert_equals([1, 2], [x for x in ll.walk()])

    def test_add_range10(self):
        ll = LinkedList()
        for i in range(9,0,-2) + range(0,10,2): ll.add_node(i)
        assert_equals(range(10), [x for x in ll.walk()])

    def test_add_negative(self):
        ll = LinkedList()
        for i in range(5) + [-10, -1, 0, 1]: ll.add_node(i)
        assert_equals([-10, -1, 0, 0, 1, 1, 2, 3, 4], [x for x in ll.walk()])

    def test_float(self):
        ll = LinkedList()
        for i in [1, 1.0, 1.1, 0.9]: ll.add_node(i)
        assert_equals([0.9, 1, 1.0, 1.1], [x for x in ll.walk()])

