# -*- coding: utf-8 -*-
"""1047.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18lv_l6kH59jp-8fkmn09P6KluCwqGEgh
"""

hi, mi, hf, mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

if hi < hf:
    h = hf - hi
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    if mi == mf:
        m = 0
if hi > hf:
    h = (24 - hi) + hf
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    if mi == mf:
        m = 0
if hi == hf:
    if mi < mf:
        m = mf - mi
        h = 0
    if mi > mf:
        m = (60 - mi) + mf
        h = 23
    if mi == mf:
        h = 24
        m = 0
    
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))