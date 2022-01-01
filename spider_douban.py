# coding=utf-8

from bs4 import BeautifulSoup
import re
import urllib.request

findNum = re.compile(r'<em class="">(.*)</em>')
findLink = re.compile(r'<a href="(.*)">')
findPic = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)
findRating = re.compile(r'<span class="rating_num".*>(.*)</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>', re.S)


def getContent():
    baseUrl = 'https://movie.douban.com/top250?start='
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

    contentList = []

    for i in range(0, 10):
        url = baseUrl + str(i * 25)
        request = urllib.request.Request(url, headers=header)
        reponse = urllib.request.urlopen(request)
        html = reponse.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            item = str(item)
            num = re.findall(findNum, item)[0]
            link = re.findall(findLink, item)[0]
            pic = re.findall(findPic, item)[0]
            title = re.findall(findTitle, item)[0]
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', '', bd)
            bd = re.sub('/', '', bd)
            bd = re.sub(r'\n', '', bd)
            bd = re.sub(r'\s+?', '', bd)
            rating = re.findall(findRating, item)[0]
            inq = re.findall(findInq, item)[0]

            contentList.append({'num': num, 'link': link, 'pic':pic, 'title': title, 'bd': bd, 'rating': rating, 'inq': inq})

        return contentList

def main():
    contentList = getContent()
    for content in contentList:
        print(content)


if __name__ == "__main__":
    main()
