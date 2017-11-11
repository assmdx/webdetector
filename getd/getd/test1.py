# -*- coding: utf-8 -*-
values = [str(v.rstrip())  for v in open('spec.txt', 'r+', encoding='utf-8').readlines() if v.rstrip()]
print(values)
