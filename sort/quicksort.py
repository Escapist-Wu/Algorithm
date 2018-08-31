# -*- coding: utf-8 -*-
import random


def quicksort(array):
    def partition(arr, left, right):
        pivot = left
        while left < right:
            while left < right and arr[right] >= arr[pivot]:
                right -= 1
            while left < right and arr[left] <= arr[pivot]:
                left += 1
            arr[left], arr[right] = arr[right], arr[left]
        arr[left], arr[pivot] = arr[pivot], arr[left]
        return left

    def qsort(arr, left, right):
        if left >= right:
            return
        pivot = partition(arr, left, right)
        qsort(arr, left, pivot)
        qsort(arr, pivot + 1, right)

    qsort(array, 0, len(array) - 1)
    return array


n = int(input())
a = [x for x in range(n)]
random.shuffle(a)
print(a)
quicksort(a)
print(a)

