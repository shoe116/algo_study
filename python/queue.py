# coding: utf-8


class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None


class Queue(object):
  def __init__(self):
    self.top = None
    self.last = None

  def enqueue(self, value):
    if self.top is None:
      self.top = Node(value)
      self.last = self.top
    else:
      self.last.next = Node(value)
      self.last = self.last.next

  def dequeue(self):
    if self.top is None:
      return None
    else:
      node = self.top
      self.top = self.top.next
      return node.value


if __name__ == "__main__":
  queue = Queue()
  queue.enqueue(1)
  queue.enqueue(2)
  queue.enqueue(3)
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())
