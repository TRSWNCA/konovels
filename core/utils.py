#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author @alex
# Description @ utils.py
# CreateTime @ 2019-12-14 21:38:55

import platform

colors = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "pink": "\033[35m",
    "cyan": "\033[36m",
    "highlight": "\033[93m",
    "error": "\033[31m",
}


def colorize(string, color):
    string = str(string)
    if color not in colors:
        return string
    if platform.system() == "Windows":
        return string
    return colors[color] + string + "\033[0m"
