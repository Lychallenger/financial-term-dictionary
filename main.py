# 请求库
import requests
# 解析库
from bs4 import BeautifulSoup


def processWords(Link):
    r = requests.get(Link)
    result = r.text
    bs = BeautifulSoup(result, 'html.parser')
    root = bs.find_all('div', id='content-well_1-0')[0]
    for child in root.children:
        if hasattr(child, 'attrs') and child.attrs['id'] == 'article_1-0':
            for child1 in child:
                if hasattr(child1, 'attrs') and child1.attrs['id'] == 'article-body_1-0':
                    for child2 in child1:
                        if hasattr(child2, 'attrs') and child2.attrs['id'] == 'mntl-sc-page_1-0':
                            for child3 in child2:
                                # 两种情况的字符串拼接
                                if hasattr(child3, 'attrs') and child3.attrs['id'] == 'mntl-sc-block_1-0':
                                    t = ""
                                    for i in range(len(child3.contents)):
                                        if hasattr(child3.contents[i], 'attr'):
                                            t += " " + child3.contents[i].contents[0].strip()
                                        else:
                                            t += " " + child3.contents[i].strip()
                                if hasattr(child3, 'attrs') and child3.attrs['id'] == 'mntl-sc-block_1-0-1':
                                    if len(child3.contents) == 0:
                                        return t
                                    else:
                                        t = ""
                                    for i in range(len(child3.contents)):
                                        if hasattr(child3.contents[i], 'attr'):
                                            t += " " + str(child3.contents[i].contents[0]).strip()
                                        else:
                                            t += " " + str(child3.contents[i]).strip()
                                    return t


def getTermWords(text,link):
    r = requests.get(link)
    print(r.status_code)
    result = r.text
    bs = BeautifulSoup(result, 'html.parser')
    divs = bs.find_all('div', id='dictionary-top300-list_1-0')
    divs = divs[0].contents[1].contents[1].contents
    with open(text, "a",encoding='utf-8') as file:
        for i in range(len(divs)):
            if i % 2 == 1 and 'href' in divs[i].attrs:
               file.write(divs[i].contents[0].contents[0]+":\n"+processWords(divs[i].attrs['href'])[1:]+"\n\n\n")

def writeTxt():
    linkPrefix='https://www.investopedia.com/terms-beginning-with-'
    linkAftfix='-476'
    lists=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'
           ,'t','u','v','w','x','y','z']
    for i in range(len(lists)):
        # i=0 -->'a'
        # i=1 -->'b'
        if i==25:#设定i获取对应的文件，全部采用for循环进程会卡住（网络的原因和网站的原因限制爬虫）
            getTermWords('data/result-'+lists[i]+'.txt',linkPrefix+lists[i]+linkAftfix+str(i+9351))


if __name__ == "__main__":
    writeTxt()
