# -*- coding: utf-8 -*-
def permutation(array):
    if len(array) == 1:
        return array[0]
    for i in range(len(array)):
         array[i] + permutation(array[0:i] + array[i + 1:])



print(permutation('123'))