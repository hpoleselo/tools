import requests
import re
import sys
from bs4 import BeautifulSoup as BS

class TideChecker(object):
        def __init__(self):
                self.response = 0
                self.highTideList = []
                self.lowTideList = []
                self.checkPage()


        def checkPage(self):
                try:
                        self.response = requests.get('https://tabuademares.com/br/bahia/lauro-de-freitas')
                        if self.response.status_code:
                                if self.response.status_code == 200:
                                        # Standard of this page will be utf-8 because it has special characters
                                        self.response.encoding = "utf-8"
                                        self.checkContent()
                                elif self.response.status_code == 204:
                                        print("Retrieved data but no content.")
                                elif self.response.status_code == 304:
                                        print("Not modified.")
                except(requests.exceptions.ConnectionError):
                        print("[ERROR]: Could not connect to the internet, network error. Check if you're connected to the internet.")
                        sys.exit(1)
                except(requests.exceptions.Timeout, requests.exceptions.ConnectTimeout):
                        print("[ERROR]: Connection timed out.")
                except requests.exceptions.HTTPError as errh:
                        print ("[ERROR]: HTTP Error:", errh)
                except(requests.exceptions.RequestException):
                        print("[ERROR]: Didn't catch the error with the previous exceptions, some brutal error is going on...")
                        sys.exit(1)


        def checkContent(self):
                pageContent = self.response.content
                # Transform the page into a string so we can parse it
                pageText = self.response.text
                self.getContent(pageText)
                print("[INFO]: Got content from webpage. ")
                

        def getContent(self, pageText):
                soup = BS(pageText, "lxml")
                container = soup.find('div', {'class' : "grafico_estado_actual_fondo"}).find('div', {'class' : "grafico_estado_actual_texto1"})

                baixaMares = container.find_all('span', {'class' : "rojo"})
                
                for baixaMar in baixaMares:
                        self.lowTideList.append(baixaMar.string)
                
                preiaMares = container.find_all('span', {'class' : "azul"})
                for altaMar in preiaMares:
                        self.highTideList.append(altaMar.string)

        def seeTides(self):
                # Temporary try because i didnt handled the previous exceptions correctly
                try:
                        high1 = self.highTideList[0] + ": " + self.highTideList[1]
                        high2 = self.highTideList[2] + ": " + self.highTideList[3]
                        low1 = self.lowTideList[0] + ": " + self.lowTideList[1]
                        low2 = self.lowTideList[2] + ": " + self.lowTideList[3]
                        return high1, high2, low1, low2
                except(IndexError):
                        print("[INFO]: Could not retrieve data from the list because maybe we're not connected to the website.")
                        high1 = "0"
                        high2 = "0"
                        low1 = "0"
                        low2 = "0"
                        return high1, high2, low1, low2

#td = TideChecker()
#td.seeTides()