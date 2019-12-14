#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author @alex
# Description @ __main__.py
# CreateTime @ 2019-12-14 21:43:28

from .tools import fuzzy_search
import importlib


def main():
    name = fuzzy_search(input())
    sources = ['quanshu']
    print("Search books from ... ")
    for s in sources:
        addon = importlib.import_module(".addons." + s)
        addon.init(name)


if __name__ == '__main__':
    main()
