# -*- coding: utf-8 -*-
"""1035.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sMsYixZEkj-RsVaSGDHHbKG4b447sVSI
"""

A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
  print('Valores aceitos')
else:
  print('Valores não aceitos')