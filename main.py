# 请求库
import requests
# 解析库
from bs4 import BeautifulSoup
# 用于解决爬取的数据格式化
import io
import sys


def processWords(Link):
    r = requests.get(Link)
    r.encoding = None
    result = r.text
    bs = BeautifulSoup(result, 'html.parser')
    root = bs.find_all('div', id='content-well_1-0')[0]
    for child in root.children:
        if hasattr(child, 'attrs') and child.attrs['id'] == 'article_1-0':
            for child1 in child:
                if hasattr(child1, 'attrs') and child1.attrs['id'] == 'article-body_1-0':
                    for child2 in child1:
                        if hasattr(child2, 'attrs') and child2.attrs['id'] == 'mntl-sc-page_1-0':
                            t = ""
                            tag=0
                            for child3 in child2:
                                # 两种情况的字符串拼接
                                if hasattr(child3, 'attrs') and child3.attrs['id'] == 'mntl-sc-block_1-0':
                                    for i in range(len(child3.contents)):
                                        if hasattr(child3.contents[i], 'attr'):
                                            t += " " + child3.contents[i].contents[0].strip()
                                        else:
                                            t += " " + child3.contents[i].strip()
                                if hasattr(child3, 'attrs') and child3.attrs['id'] == 'mntl-sc-block_1-0-1':
                                    t = ""
                                    for i in range(len(child3.contents)):
                                        t += " " + child3.contents[i].strip()
                                    tag=1
                                    break
                            if tag==1:
                                break
    # Todo
    # 输出有点问题
    print(t)


def getTermWords():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    # 爬取的网页链接
    r = requests.get("https://www.investopedia.com/terms-beginning-with-a-4769351")
    # 类型
    # print(type(r))
    print(r.status_code)
    # 中文显示
    # r.encoding='utf-8'
    r.encoding = None
    result = r.text
    bs = BeautifulSoup(result, 'html.parser')
    divs = bs.find_all('div', id='dictionary-top300-list_1-0')
    divs = divs[0].contents[1].contents[1].contents
    for i in range(len(divs)):
        if i % 2 == 1 and 'href' in divs[i].attrs:
            # 测试标签第9个,1,3,5,7,9
            if i == 9:
                processWords(divs[i].attrs['href'])


if __name__ == "__main__":
    getTermWords()
