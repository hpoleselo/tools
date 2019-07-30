import requests
import re
import sys
from bs4 import BeautifulSoup as BS

class TideChecker(object):
        def __init__(self):
                self.response = 0
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
                except(requests.exceptions.ConnectionError, ConnectionError): #P q Connectionerroe nao eh levado em conta?
                        print("Could not connect to the internet, network error. Check if you're connected to the internet.")
                        # Do something to not run the other programs on our telegram
                except(requests.exceptions.Timeout, requests.exceptions.ConnectTimeout):
                        print("Connection timed out.")
                except(requests.exceptions.RequestException):
                        print("Didn't catch the error with the previous exceptions, some brutal error is going on...")
                        sys.exit(1)

        def checkContent(self):
                pageContent = self.response.content
                # Transform the page into a string so we can parse it
                pageText = self.response.text
                self.getContent(pageText)
                

        def getContent(self, pageText):
                soup = BS(pageText, "lxml")
                container = soup.find('div', {'class' : "grafico_estado_actual_fondo"}).find('div', {'class' : "grafico_estado_actual_texto1"})

                baixaMar = container.find_all('span', {'class' : "rojo"})

                for lowTide in baixaMar:
                        print(lowTide.string)
                
                preiaMar = container.find_all('span', {'class' : "azul"})

                for highTide in preiaMar:
                        print(highTide.string)


def run():
        TideChecker()

if __name__ == "__main__":
        run()