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
                        self.response = requests.get('https://pt.surf-forecast.com/breaks/Vilas/forecasts/latest/six_day')
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

        def getContent(self, pageText):
                soup = BS(pageText, "lxml")

                # Exemplo anterior:
                #container = soup.find('div', {'class' : "grafico_estado_actual_fondo"}).find('div', {'class' : "grafico_estado_actual_texto1"})
                #baixaMares = container.find_all('span', {'class' : "rojo"})

                #TODO
                # Periodo: <tr class=forecast-table__row data-row-name=""periods"> contem <td class="forecast-table__cell"><strong>8</strong></td> -> <strong>8</strong>

                # Energia da onda: <tr class="forecast-table__row" data-row-name="energy"><td class="forecast-table__cell forecast-table-energy__cell"  


                

# For debugging purposes without using Telegram's Bot
td = TideChecker()
td.checkContent()