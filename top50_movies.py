#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from lxml import etree
from prettytable import PrettyTable

latest_movies_url = "http://www.6vhao.tv/top.html"
ROWS = 25
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}


def getTop50():
    """
    :return:
    """
    response = requests.get(latest_movies_url, headers=headers)
    webContentEncode = response.apparent_encoding
    response.encoding = webContentEncode
    html = response.text
    selector = etree.HTML(html)
    result = selector.xpath('//div[@class="listBox"]//tr//a[@target="_blank"]/@title')
    table = PrettyTable()
    index = 0
    for i in result[::ROWS]:
        rest_column = [j for j in result[index + 1:index + ROWS]]
        table.add_column(i, rest_column)
        index += ROWS
    print(table)


if __name__ == '__main__':
    getTop50()
