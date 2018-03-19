# coding: utf-8
from base_sort import BaseSort


class HeapSort(BaseSort):
  @classmethod
  def sort(cls, array=[]):
    cls.build_heap(array)

    i = len(array) - 1
    while i >= 0:
      array[i], array[0] = array[0], array[i]
      cls.heapify(array, 0, i)
      i -= 1

  @classmethod
  def build_heap(cls, array):
    i = int(len(array) / 2) - 1
    while i >= 0:
      cls.heapify(array, i, len(array))
      i -= 1


  @classmethod
  def heapify(cls, array, start, end):
    ## init
    largest_id = start
    left_node_id = 2 * start + 1
    right_node_id = 2 * start + 2

    if left_node_id < end and array[left_node_id] > array[largest_id]:
      largest_id = left_node_id
    if right_node_id < end and array[right_node_id] > array[largest_id]:
      largest_id = right_node_id

    if start != largest_id: ## if largest is updated
      array[largest_id], array[start] = array[start], array[largest_id]
      cls.heapify(array, largest_id, end)


if __name__ == "__main__":
  input_array = [1, 6, 4, 7, 0, 2, 2]
  print(input_array)
  HeapSort.sort(input_array)
  print(input_array)
