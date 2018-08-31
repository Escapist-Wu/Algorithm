# -*- coding: utf-8 -*-
import random


def selectionsort(array):
    for i in range(len(array)):
        min_index = i
        for k in range(i + 1, len(array)):
            if array[k] < array[min_index]:
                min_index = k
        array[i], array[min_index] = array[min_index], array[i]
    return array


a = [x for x in range(10)]
random.shuffle(a)
print(a)
selectionsort(a)
print(a)
