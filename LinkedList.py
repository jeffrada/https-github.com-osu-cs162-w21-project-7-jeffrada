# Author: Adam Jeffries
# Date: 2/16/2021
# Description: A class that utilizes multiple recursive methods add, remove, contains, insert and reversal

class Node:
    """
    node stores data and the next value
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList:
    """
    class linked list
    """

    def __init__(self):
        self.__head = None

    def get_head(self):
        return self.__head

    def set_head(self, head):
        self.__head = head

    def add_recursively(self, a_node, val):
        """
        An add method utilizing recursion
        """
        if a_node.next is None:
            a_node.set_next(Node(val))
        else:
            self.add_recursively(a_node.next, val)

    def add(self, val):
        """
        Calls add method and verifies that the head is assigned to the node
        """
        if self.__head is None:
            self.set_head(Node(val))
        else:
            self.add_recursively(self.__head, val)

    def rec_display(self, a_node):
        """
        recursive display method
        """

        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def remove(self, a_node, val = None):
        """
        A remove method utilizing recursion
        """
        if val is None:
            val = a_node.data
        if self.__head.data == val:
            self.set_head(self.__head.next)
            return
        if a_node.next is None:
            return
        elif a_node.next.data == val:
            a_node.set_next(a_node.next.next)
            return
        else:
            self.remove(a_node.next, val)

    def contains(self, a_node, val):
        if a_node.data == val:
            return True
        if a_node.next is None:
            return False
        return self.contains(a_node.next, val)

    def insert(self, a_node, index, val, init):
        """
        Inserts an element at a particular index
        """
        if index == 0:
            self.set_head(Node(val, self.head))
            return
        elif a_node.next is None:
            a_node.set_next(Node(val))
        elif index == init + 1:
            no = Node(val)
            no.set_next(a_node.next)
            a_node.set_next(no)
        else:
            self.insert(a_node.next, index, val, init + 1)

    def _rev(self, a_node):
        """
        Method used for reversal
        """
        if a_node is None or a_node.next is None:
            return a_node
        t_node = self._rev(a_node.next)
        a_node.next.set_next(a_node)
        a_node.set_next(None)
        return t_node

    def reverse(self):
        """
        Another method  which assigns the head of a reversed last node to the first node
        """
        self.set_head(self._rev(self.__head))

    def to_plain_list(self, a_node):
        """
        to convert data into a list and returning it
        """
        if a_node.next is not None:
            lst = self.to_plain_list(a_node.next)
        elif a_node.next is None:
            return [a_node.data]
        a = []
        a.append(a_node.data)
        a = a.__add__(lst)
        return a
