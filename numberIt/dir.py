#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

splash = r'\ '[:-1]

changeDir = input('enter the dir: ')
filename = input('enter the filename(spliter: 0): ')

prefix, postfix = filename.split('0')

if '/' in changeDir:
    if changeDir[-1] != '/':
        changeDir += '/'
elif splash in changeDir:
    if changeDir[-1] != splash:
        changeDir += splash

toChange = os.listdir(changeDir)

for i, item in enumerate(toChange):
    os.rename(changeDir+item, changeDir+prefix+str(i+1)+postfix)
