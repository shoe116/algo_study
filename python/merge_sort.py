from base_sort import BaseSort


class MergeSort(BaseSort):
  @classmethod
  def sort(cls, array=[]):
    copy = list(array)
    cls.marge_sort(copy, array, 0, len(array))

  @classmethod
  def marge_sort(cls, target_array, result_array, start, end):
    if end - start < 2:
      return
    elif end - start == 2:
      if result_array[start] > result_array[end - 1]:
        result_array[start], result_array[end - 1] = result_array[end - 1], result_array[start]
      return
    else:
      mid = int((start + end) / 2)
      cls.marge_sort(result_array, target_array, start, mid)
      cls.marge_sort(result_array, target_array, mid, end)

    ## marge
    small_index = start
    large_index = mid
    index = start
    while index < end:
      if small_index < mid and large_index < end:
        if target_array[small_index] <= target_array[large_index]:
          result_array[index] = target_array[small_index]
          small_index += 1
        else:
          result_array[index] = target_array[large_index]
          large_index += 1
      elif small_index == mid and large_index < end:
        result_array[index] = target_array[large_index]
        large_index += 1
      elif large_index == end and small_index < mid:
        result_array[index] = target_array[small_index]
        small_index += 1
      else:
        raise Exception("bug")

      index += 1


if __name__ == "__main__":
  input_array = [1, 6, 4, 7, 0, 2, 2]
  print(input_array)
  MergeSort.sort(input_array)
  print(input_array)
