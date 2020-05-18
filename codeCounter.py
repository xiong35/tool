# -*- coding: UTF-8 -*-

import os
import re

lang_map = {
    ".py": r"^#",
    ".vue": r"^//",
    ".js": r"^//",
    ".c": r"^//",
    ".kt": r"^//",
    ".cpp": r"^//",
    ".h": r"^//",
    ".css": r"/\*.*\*/",
    ".html": r"^ *<!--",
    ".cs": r"^//",
    ".java": r"^//",
}

excludes = [r".*\\dist.*", r".*\\node_modules.*", r".*\\\..*",
            r".*\\log.*", r".*\\info.*", r".*\\assets.*", r".*\\migrations.*",
            r".*\\front_alias.*", r".*\\homework.*"]

langs = lang_map.keys()


line_num = 0
file_num = 0


def walk(directory):
    for root, dirs, files in os.walk(directory):
        for exclude in excludes:
            if re.match(exclude, root):
                files = []
                break
        for name in files:
            name_ = os.path.join(root, name)
            for lang in langs:
                if name_.endswith(lang):
                    count(name_, lang)
                    break


def count(file_name, lang):
    if file_name.endswith("tempCodeRunnerFile.py"):
        return
    try:
        with open(file_name, "r", encoding="utf-8") as fr:
            lines = fr.readlines()
    except UnicodeDecodeError:
        return
    r = lang_map[lang]

    global line_num
    global file_num

    old = line_num

    for line in lines:
        if not re.match(r, line) and line:
            line_num += 1
    file_num += 1
    print(file_name, line_num-old)


target_dir = input("enter target directory: ")
walk(target_dir)

print("-------")
print("file num:", file_num)
print("line num:", line_num)
