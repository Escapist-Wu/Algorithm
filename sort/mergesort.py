# -*- coding: utf-8 -*-
import random


def mergesort(array):
    def merge(arr, left, mid, right):
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        arr[left: right + 1] = temp[0:]

    def divide(arr, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        divide(arr, left, mid)
        divide(arr, mid + 1, right)
        merge(arr, left, mid, right)

    divide(array, 0, len(array) - 1)


a = [x for x in range(10)]
random.shuffle(a)
print(a)
mergesort(a)
print(a)
