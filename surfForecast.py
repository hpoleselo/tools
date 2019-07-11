import requests
import re
from bs4 import BeautifulSoup as BS

class TideChecker(object):
        def __init__(self):
                self.response = 0
                self.checkPage()
                self.pattern = "preia-mar"
                self.bora = "itcha"

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
                        else:
                                print("Could not connect to the webpage.")
                except(AttributeError):
                        print("Not connected to the internet.")

        def checkContent(self):
                #print(self.bora)
                pageContent = self.response.content
                # Transform the page into a string so we can parse it
                pageText = self.response.text
                self.getContent(pageText)
                

        def getContent(self, pageText):
                soup = BS(pageText)
                # Searching for the div id!
                highTide1 = soup.find("div", {"id" : "grafico_estado_actual_texto_pleamar"})
                print (highTide1)
                lowTide1 = soup.find("div", {"id" : "grafico_estado_actual_texto_bajamar"})
                print(lowTide1)
                highTide2 = soup.find("div", {"class" : "tabla_mareas_marea_hora tabla_mareas_hora_bajamar"})
                print(highTide2)

        def searchPattern(self, pageText):
                """ Deprecated... using BeautifulSoup! """
                #pattern = self.pattern
                pattern="preia-mar"
                pattern2="baixa-mar"
                smth = re.findall(pattern, pageText)
                smth2 = re.findall(pattern2, pageText)
                # quando encontrar a palavra, procurar a key q ela se encontra e pegar essa posicao
                print (smth)
                print (smth2)



def run():
        TideChecker()

if __name__ == "__main__":
        run()