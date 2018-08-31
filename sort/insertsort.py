# -*- coding: utf-8 -*-
import random


def insertsort(array):
    for i in range(len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array


a = [x for x in range(10)]
random.shuffle(a)
print(a)
insertsort(a)
print(a)
