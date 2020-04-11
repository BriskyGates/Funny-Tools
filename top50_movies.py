#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml import etree
from prettytable import PrettyTable

latest_movies_url = "http://www.6vhao.tv/top.html"
ROWS=10  # 总行数

def getTop50():
    """
    在美观打印电影名时,做了取舍,直接将字段名变成每组第一个电影名
    :return: 
    """
    response = requests.get(latest_movies_url)
    webContentEncode = response.apparent_encoding  # 获取网页内容的编码
    response.encoding = webContentEncode
    html = response.text
    selector = etree.HTML(html)
    result = selector.xpath('//div[@class="listBox"]//tr//a/@title')  # 获取top50 的电影名字
    table = PrettyTable()
    index = 0
    for i in result[::ROWS]:
        rest_column = [j for j in result[index + 1:index + ROWS]]
        table.add_column(i, rest_column)
        index += 5
    print(table)


if __name__ == '__main__':
    getTop50()
