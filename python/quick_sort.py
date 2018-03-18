# coding: utf-8
from base_sort import BaseSort


class QuickSort(BaseSort):
  @classmethod
  def sort(cls, array=[]):
    cls.quick_sort(array, 0, len(array) - 1)

  @classmethod
  def quick_sort(cls, array, left, right):
    if left < right:
      pi, pivot_val = cls.partition(array, left, right)
      cls.quick_sort(array, left, pi - 1)
      cls.quick_sort(array, pi + 1, right)

  @staticmethod
  def partition(array, left, right):
    if right - left == 1:
      if array[left] > array[right]:
        tmp = array[left]
        array[left] = array[right]
        array[right] = tmp

      return right, array[right]

    ## init
    pivot_val = array[left]
    pivot_index = left
    index = left
    end = right
    while index <= right:
      tmp = array[index]
      if tmp > pivot_val:
        array[index] = array[end]
        array[end] = tmp
        end -= 1
        if index == end:
          break
      else:
        pivot_index = index
        index += 1
    # swap left to index
    array[left] = array[pivot_index]
    array[pivot_index] = pivot_val

    return pivot_index, pivot_val


if __name__ == "__main__":
  input_array = [1, 6, 4, 7, 0, 2, 2]
  print(input_array)
  QuickSort.sort(input_array)
  print(input_array)
