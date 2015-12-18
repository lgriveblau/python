#!/usr/bin/python
# -*- coding: utf-8 -*-
fh = open('prueba.txt', 'r')
print fh

count = 0
lcount = 0
rcount = 0
nombre[2][4] 
for line in fh:
    pos = line.find('-')
    spos = line.find(': ')
    nom = line[pos + 2:spos]
    if nom == 'Luis Rivero Blanco-Uribe':
        lcount += 1
    elif nombre == 'Ra\xc3\xbal Iturra':
        rcount += 1
    count += 1
print count, lcount, rcount