#!/usr/bin/python
# -*- coding: utf-8 -*-
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
sppos = data.find(' ', atpos)
host = data[atpos + 1:sppos]
print host