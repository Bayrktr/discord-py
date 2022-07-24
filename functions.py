import requests
from bs4 import BeautifulSoup
import random

rutin = 1000


def connectWebSite(ZodiacSignName):
    def webSiteCheck(ZodiacSignName):
        a = requests.head("https://www.alem.com.tr/astroloji/{}-burcu-gunluk-burc-yorumu".format(ZodiacSignName))
        return a.status_code == 200

    if webSiteCheck(ZodiacSignName):
        a = requests.get("https://www.alem.com.tr/astroloji/{}-burcu-gunluk-burc-yorumu".format(ZodiacSignName))
        a = a.text
        soup = BeautifulSoup(a, "html.parser")
        value = soup.find("div", attrs={"class": "content font-size-16 margin-bottom-md"})
        value = soup.find_all("p", value)
        value = value[1]
        return value.text
    else:
        return "Servis Kullanım Dışı"


def animenizNews():
    def links():
        link = []
        a = requests.get('https://pudiperi.com/')
        a = a.text
        soup = BeautifulSoup(a, 'html.parser')
        value = soup.find('div', attrs={'class': 'col-md-12'})
        value = soup.find_all('a', value, href=True)
        for x in value:
            link.append(x['href'])
        link = link[31]
        return link

    def newContent():
        number = 0
        contentList = ''
        x = links()
        a = requests.get(x)
        a = a.text
        soup = BeautifulSoup(a, 'html.parser')
        value = soup.find('div', attrs={'class': 'entry-content'})
        value = soup.find_all('p', value)
        print(value)
        for _ in range(5):
            value.pop(len(value) - 1)
        for y in value:
            number += len(list(y.text))
            print(number)
            if number < 1900:
                contentList += str(y.text)
            else:
                contentList += '..'
                break
        return contentList, x

    return newContent()


def animeNews():
    def animeLink():
        links = []
        a = requests.get('https://www.animerkez.com/')
        a = a.text
        soup = BeautifulSoup(a, 'html.parser')
        value = soup.find('div', attrs={'class': 'nr-post nr-post-with-number nr-d-flex'})
        value = soup.find_all('a', value, href=True)
        for x in value:
            links.append(x['href'])
        value = links[0]
        return value

    def newContent():
        def title():
            titleValue = soup.find('header', attrs={'class': 'entry-header entry-header-1'})
            titleValue = soup.find('h1')
            titleValue = titleValue.text.strip()
            return titleValue

        contentList = []
        link = animeLink()
        a = requests.get(link)
        a = a.text
        soup = BeautifulSoup(a, 'html.parser')
        mainValue = soup.find('div', attrs={'class': 'post-content-wrap'})
        value = soup.find_all('p', mainValue)
        for x in value:
            if x == '':
                pass
            else:
                contentList.append(x.text)
        print(title())
        for _ in range(2):
            contentList.pop(0)
        word = ''
        number = 0
        for x in contentList:
            print(x)
            number += len(list(x))
            if number <= 1950:
                word += str(x)
            else:
                break
        contentList = word
        return contentList, title(), link

    return newContent()


def gameNews():
    def link():
        links = []
        a = requests.get("https://shiftdelete.net/oyun")
        a = a.text
        soup = BeautifulSoup(a, "html.parser")
        value = soup.find("div", attrs={"class": "sidebar-content-main"})
        value = soup.find_all("a", value, href=True)
        for x in value:
            links.append(x["href"])
        links = links[18]
        return links

    def newsContent():
        def pictureLink():
            pictureValue = soup.find_all("img", Mainvalue)
            pictureValue = pictureValue[5]["src"]
            return pictureValue

        contentList = []
        contentLink = link()
        a = requests.get(contentLink)
        a = a.text
        soup = BeautifulSoup(a, "html.parser")
        Mainvalue = soup.find("div", attrs={"class": "sidebar-content-main"})

        value = soup.find_all("p", Mainvalue)
        for x in value:
            if x.text == "":
                break
            else:
                contentList.append(x.text)

        # 2000 word check

        wordNumber = 8 + len(list(contentList))
        wordNumber -= len(contentList[len(contentList) - 1])
        title = contentList[0]
        contentList.pop(0)
        newContentList = []
        wordNumber += len(title)
        for x in contentList:
            if wordNumber + len(x) < 2000:
                newContentList.append(x)
            else:
                break
        newContentList.pop()
        newContentList = "".join(newContentList)
        return title, newContentList, pictureLink(), contentLink

    return newsContent()


def takeGif(name):
    def link(name):
        links = []
        a = requests.get("https://tenor.com/search/{}-gifs".format(name)).text
        soup = BeautifulSoup(a, 'html.parser')
        all_imgs = soup.find_all('img', src=True)
        for image in all_imgs:
            links.append(image['src'])
        return links

    return random.choice(link(name))


def weatherDatas(city):
    def link(city):
        return 'https://www.mynet.com/hava-durumu/{}-hava-durumu-bugun'.format(city)

    def title(soup):
        value = soup.find('h3', attrs={'class': 'heading mb-2'})
        return value.text

    def txt(soup):
        def weatherTitle(value):
            mainTitleTxt = ""
            for x in list(value):
                if x == ":":
                    break
                else:
                    mainTitleTxt += x
            return mainTitleTxt

        value = soup.find('p', attrs={'class': 'mb-0'})
        value = value.text
        return value, weatherTitle(value),title(soup)

    a = requests.get(link(city))
    if a.status_code == 404:
        return "Bu isme sahip bir şehir bilmiyorum hmm farklı bir gezegende olmasın :smile:"
    else:
        weatherEmoji = ''
        color = ''
        
        a = a.text
        soup = BeautifulSoup(a, 'html.parser')
        datas = []
        datas.append(txt(soup))
        if datas[0][2] == 'Açık':
            weatherEmoji = ':sunny:'
            color = 0xf1c40f
        elif datas[0][2] == 'Kapalı':
            weatherEmoji = ':cloud:'
            color = 0
        elif datas[0][2] == 'Hafif Yağmur':
            weatherEmoji = ':cloud_rain:'
            color = 0x3498db
        elif datas[0][2] == 'Az Bulutlu':
            weatherEmoji = ':white_sun_cloud:'
            color = 0
        else:
            weatherEmoji = 'Uygun emoji bulunamadı lutfen sahibime bildir.'
            color = 0
        datas = list(datas)
        datas[0] = list(datas[0])
        datas[0][2] += weatherEmoji
        datas.append(color)
        return datas


print(weatherDatas('kutahya'))
