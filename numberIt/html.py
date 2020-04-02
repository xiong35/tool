#!/usr/bin/env python

import re

filename = input('enter the HTML file name: ')
toChange = input('enter what to change: ')

with open(filename, 'r') as fr:
    lines = fr.readlines()

i = 0
while (lines[i].strip() != '<!-- begin_ -->'):
    i += 1

lines.pop(i)

j = 1
while (lines[i].strip() != '<!-- end_ -->'):
    lines[i] = re.sub(toChange, toChange+str(j), lines[i])
    i += 1
    j += 1

lines.pop(i)

with open(filename, 'w') as fw:
    for line in lines:
        fw.write(line)
