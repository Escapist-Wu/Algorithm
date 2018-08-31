# -*- coding: utf-8 -*-
import random


def shellsort(array):
    d = len(array) // 2
    while d > 0:
        for i in range(d, len(array)):
            current = array[i]
            j = i - d
            while j >= 0 and array[j] > current:
                array[j + d] = array[j]
                j -= d
            array[j + d] = current
        d = d // 2
    return array


a = [x for x in range(10)]
random.shuffle(a)
print(a)
shellsort(a)
print(a)



