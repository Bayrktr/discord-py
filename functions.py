import requests
from bs4 import BeautifulSoup


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


def takeZodiacSignName():
    print()


ZodiacSignName = "terazi"
connectWebSite(ZodiacSignName)
