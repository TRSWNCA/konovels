#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author @alex
# Description @ tools.py
# CreateTime @ 2019-12-14 21:41:19

from urllib.request import quote

import requests
from bs4 import BeautifulSoup as soup


def fuzzy_search(sName) -> (str):
    """return an accurate name
    """
    sName = quote(sName.strip().encode('utf-8'))
    QidianUrl = 'https://www.qidian.com/search?kw='
    html = requests.get(QidianUrl + repr(sName)[1:-1])
    html.encoding = 'utf-8'
    bsObj = soup(html.text, features='lxml')
    search_resname = []
    for search_res in bsObj.findAll("h4"):
        search_resname.append(search_res.get_text())
    for num, _ in enumerate(reversed(search_resname)):
        print("\033[1;35m [%02d] \033[0m %s" %
              (len(search_resname) - num - 1, _))
    resnum = input(">> 请选择结果: ")
    return search_resname[int(resnum)]
