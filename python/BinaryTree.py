# coding: utf-8


class BinaryNode(object):
  def __init__(self, value):
    self.value = value
    self.left_node = None
    self.right_node = None

  def add(self, value):
    if value <= self.value:
      if self.left_node is None:
        self.left_node = BinaryNode(value)
      else:
        self.left_node.add(value)
    else:
      if self.right_node is None:
        self.right_node = BinaryNode(value)
      else:
        self.right_node.add(value)

  def get_value(self):
    return self.value

  def get_left_node(self):
    return self.left_node

  def get_right_node(self):
    return self.right_node


class BinaryTree(object):
  def __init__(self):
    self.root = None

  def add(self, value):
    if self.root is None:
      self.root = BinaryNode(value)
    else:
      self.root.add(value)

  def has(self, value):
    return self.contains(self.root, value)

  @classmethod
  def contains(cls, top_node, value):
    if top_node is None:
      return False
    else:
      node_value = top_node.get_value()
      if value < node_value:
        return cls.contains(top_node.get_left_node(), value)
      elif value > node_value:
        return cls.contains(top_node.get_right_node(), value)
      else:
        return True


if __name__ == "__main__":
  # init
  binary_tree = BinaryTree()
  print(binary_tree.has(4))
  # add root
  binary_tree.add(4)
  print(binary_tree.has(4))

  # add values
  binary_tree.add(5)
  binary_tree.add(8)
  binary_tree.add(0)
  binary_tree.add(1)
  binary_tree.add(6)
  binary_tree.add(4)

  print(binary_tree.has(6))
  print(binary_tree.has(7))
  print(binary_tree.has(8))
