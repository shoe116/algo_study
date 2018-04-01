# coding: utf-8
from base_sort import BaseSort


class QuickSort(BaseSort):
  @classmethod
  def sort(cls, array=[]):
    cls.quick_sort(array, 0, len(array) - 1)

  @classmethod
  def quick_sort(cls, array, left, right):
    if left < right:
      pivot_index = cls.partition(array, left, right)
      cls.quick_sort(array, left, pivot_index - 1)
      cls.quick_sort(array, pivot_index + 1, right)

  @staticmethod
  def partition(array, left, right):
    if right - left == 1:
      if array[left] > array[right]:
        array[left], array[right] = array[right], array[left]
      return left

    ## init
    pivot_val = array[left]
    end = right
    index = left
    while index <= end:
      tmp = array[index]
      if tmp > pivot_val:
        array[index], array[end] = array[end], array[index]
        end -= 1
      else:
        index += 1
    # swap left to index
    pivot_index = max(index - 1, left)
    array[left],  array[pivot_index] = array[pivot_index], array[left]

    return pivot_index


if __name__ == "__main__":
  input_array = [0, 1, 6, 4, 7, 0, 2, 2]
  print(input_array)
  QuickSort.sort(input_array)
  print(input_array)
