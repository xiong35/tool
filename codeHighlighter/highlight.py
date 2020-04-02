#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
import changeDict
import template


class Formater:

    def loadCode(self, code):
        while not code[0].strip():
            code.pop(0)
        while not code[-1].strip():
            code.pop()
        i = -1
        while True:
            try:
                i += 1
                if code[i] == '\n'and code[i+1] == '\n':
                    code.pop(i)
            except IndexError:
                break

        self.lines = len(code)
        self.code = ''
        for line in code:
            self.code += line

    def mainHandel(self, code, dest, full=True):
        self.loadCode(code)
        colText = self.creatTable()
        self.parseCode()
        html = template.tableHTML.format(colText, self.code)
        if full:
            html = template.fullHTML.format(html)
        with open(dest, 'w') as fw:
            fw.write(html)

    def creatTable(self,):
        colText = '\n'.join(map(str, range(1, self.lines+1)))
        return colText

    def parseCode(self):
        for item in changeDict.changes:
            def change2Span(matched):
                value = matched.group('value')
                returnMsg = f'<span class="{item["className"]}">{value}</span>'
                try:
                    returnMsg = item['add'][0]+returnMsg+item['add'][1]
                except KeyError:
                    pass
                return returnMsg
            self.code = re.sub(item['pat'], change2Span, self.code)


if not os.path.exists('./dest'):
    os.mkdir('./dest')

formater = Formater()

formater.mainHandel(sys.stdin.readlines(), './dest/out.html')
