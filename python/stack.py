# coding: utf-8


class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None


class Stack(object):
  def __init__(self):
    self.top = None

  def push(self, value):
    if self.top is None:
      self.top = Node(value)
    else:
      node = self.top
      self.top = Node(value)
      self.top.next = node

  def pop(self):
    if self.top is None:
      return None
    else:
      node = self.top
      self.top = node.next
      return node.value

  def peek(self):
    if self.top is None:
      return None
    else:
      return self.top.value


if __name__ == "__main__":
  stack = Stack()
  stack.push(1)
  stack.push(2)
  print(stack.peek())
  print(stack.pop())
  print(stack.peek())
  stack.push(3)
  print(stack.pop())
  print(stack.peek())
