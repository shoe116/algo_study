import sys
sys.path.append('python')
from merge_sort import MergeSort


def test_merge_sort_basic():
    arr = [5, 3, 1, 4, 2]
    MergeSort.sort(arr)
    assert arr == [1, 2, 3, 4, 5]


def test_merge_sort_with_negatives_and_duplicates():
    arr = [3, -2, 4, -5, 0, 3]
    MergeSort.sort(arr)
    assert arr == [-5, -2, 0, 3, 3, 4]
