from bs4 import BeautifulSoup as soup
from urllib.request import quote

import requests


def getAccurateName(book_name):
    """fuzzy search supported"""
    book_name = quote(book_name.strip().encode('utf-8'))
    QidianUrl = 'https://www.qidian.com/search?kw='
    html = requests.get(QidianUrl + repr(book_name)[1:-1])
    html.encoding = 'utf-8'
    bsObj = soup(html.text, features='lxml')
    search_resname = []
    search_resurl = []
    for search_res in bsObj.findAll("h4"):
        search_resname.append(search_res.get_text())
        search_resurl.append(search_res.contents[0]['href'])
    for num, _ in enumerate(reversed(search_res)):
        print("\033[1;35m [%02d] \033[0m %s" % (len(search_res) - num - 1, _))
    resnum = input(">> 请选择结果: ")
    return search_resname[int(resnum)]
