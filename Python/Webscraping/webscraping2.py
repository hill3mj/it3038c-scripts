from bs4 import BeautifulSoup
import requests, re


r = requests.get("https://www.worldometers.info/coronavirus/").content
soup = BeautifulSoup(r, "lxml")
span = soup.find_all("div", {"class":"maincounter-number"})
totalCases = span[0].text
totalDeaths = span[1].text
totalRecovered = span[2].text
print("There are" + totalCases + "total coronavirus cases.\n")
print("There are" + totalDeaths + "total coronavirus deaths.\n")
print("There are" + totalRecovered + "total people recovered from coronavirus")