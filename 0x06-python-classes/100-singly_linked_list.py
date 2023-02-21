#!/usr/bin/python3

class Node:
  '''A singly linked list class'''
  def __init__(self, data, next_node=None):
    self.__data = data
    self.__next_node = next_node

  @property
  def data(self):
    return self.__data

  @data.setter
  def data(self, value):
    if type(value) != int:
      raise TypeError("data must be an integer")
    self.__data = value

  @property
  def next_node(self):
    return self.__next_node
  
  @next_node.setter
  def next_node(self, value):
    if not isinstance(value, Node) and value != None:
      raise TypeError("next_node must be a Node object")
    self.__next_node = value


class SinglyLinkedList:

  def __init__(self):
    self.__head = None
  
  def sorted_insert(self, value):
    new = Node(value)
    if self.__head == None:
      new.next_node = None
      self.__head = new
    else:
      temp = self.__head
      while temp.next_node and new.data > temp.next_node.data:
          temp = temp.next_node
      new.next_node = temp.next_node
      temp.next_node = new

  def __str__(self):
    ''' Define print() '''
    values = []
    temp = self.__head
    while temp:
      values.append(str(temp.data))
      temp = temp.next_node
    return ('\n'.join(values))

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
