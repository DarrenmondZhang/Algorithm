import random
import numpy as np


def selection_sort(sequence):
    """Pure implementation of the selection sort algorithm in Python

    Args:
        sequence: An unsorted array
    
    Returns:
        The same array ordered by ascending

    """
    n = len(sequence)
    for i in range(n-1):
        min_idx = i  # We assume that the element of i index is the smallest
        for j in range(i+1, n):  # iterate from i + 1 position to n-1 position
            if sequence[j] < sequence[min_idx]:
                min_idx = j
        if min_idx != i:
            sequence[i], sequence[min_idx] = sequence[min_idx], sequence[i]
    return sequence


def bubble_sort(sequence):
    """Pure implementation of the Bubble sort algorithm in Python

    Args:
        sequence: An unsorted array
    
    Returns:
        The same array ordered by descending

    """
    n = len(sequence)
    for i in range(n-1):
        print(sequence)
        for j in range(n-1-i):
            if sequence[j] > sequence[j+1]:
                sequence[j+1], sequence[j] = sequence[j], sequence[j+1]
    return sequence


def insertion_sort(sequence):
    """Pure implementation of the Bubble sort algorithm in Python
    每次将元素插入到已经有序的数组中，初始时已经有序的数组长度为1

    Args:
        sequence: An unsorted array
    
    Returns:
        The same array ordered by descending

    """
    for i in range(1, len(sequence)):
        print(i)
        while i > 0 and sequence[i] < sequence[i-1]:
            sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
            i -= 1
            print(sequence)
    return sequence


def merge_sort(sequence):
    """Pure implementation of the Bubble sort algorithm in Python
    将两个序列，左边排好序，右边排好序，然后再让其整体有序， 递归过程

    Args:
        sequence: An unsorted array
    
    Returns:
        An new array ordered by descending

    """
    if len(sequence) <= 1: # 只有当一个元素时，是递归的出口
        return sequence
    else:
        mid = int(len(sequence) / 2) 
        left_half = merge_sort(sequence[:mid])
        right_half = merge_sort(sequence[mid:])

        # Merge two ordered arrays
        new_sequence = merge(left_half, right_half)
        return new_sequence


def merge(sorted_a, sorted_b):
    """ 合并两个序列，返回一个新的有序序列

    Args:
        Two arrays

    Returns:

    """
    len_a = len(sorted_a)
    len_b = len(sorted_b)
    a = b = 0
    new_sequence = list()
    while a < len_a and b < len_b:
        if sorted_a[a] < sorted_b[b]:
            new_sequence.append(sorted_a[a])
            a += 1
        else:
            new_sequence.append(sorted_b[b])
            b += 1

    # 最后别忘记把多余的都放到有序数组里
    if a < len_a:
        new_sequence.extend(sorted_a[a:])
    else:
            new_sequence.extend(sorted_b[b:])

    return new_sequence


if __name__ == "__main__":
    seq = list(range(11))  # 注意 python3 返回迭代器，所以我都用 list 强转了，python2 range 返回的就是list
    random.shuffle(seq)  # shuffle inplace 操作，打乱数组
    # new_seq = np.array(seq)
    print(seq)
    # print(selection_sort(seq))
    # print(bubble_sort(seq))
    # print(insertion_sort(seq))
    print(merge_sort(seq))




