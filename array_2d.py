# -*- coding:utf-8 -*-
n = int(input())
a = [[] for i in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
print(a)
