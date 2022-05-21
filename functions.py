import requests
from bs4 import BeautifulSoup

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
            for x in pictureValue:
                print(x["src"])
            pictureValue = pictureValue[5]["src"]
            return pictureValue

        contentList = []
        a = requests.get(link())
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

        wordNumber = 2 + 8
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
        return title, newContentList, pictureLink()

    return newsContent()
