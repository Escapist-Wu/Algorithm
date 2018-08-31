# -*- coding: utf-8 -*-
import random


def bubblesort(array):
    for i in range(len(array), 0, -1):
        for k in range(1, i):
            if array[k] < array[k - 1]:
                array[k], array[k - 1] = array[k - 1], array[k]
    return array


a = [x for x in range(10)]
random.shuffle(a)
print(a)
bubblesort(a)
print(a)

