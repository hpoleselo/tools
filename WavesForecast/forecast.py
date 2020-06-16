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

                period = []
                energy = []
                wave_height = []
                wind = []
                wind_state = []
                # TODO: usar dictionary pro wind e wind direction
                wind_direction = []

                # find_all retorna um iteravel, por isso precisamos passar por um for

                # Wave period
                forecastTableRows = soup.find_all("tr", {"data-row-name":"periods"})
                for tableRow in forecastTableRows:
                        tableCells = tableRow.find_all('td', class_='forecast-table__cell')
                        for cell in tableCells:
                                value = cell.find("strong").text
                                period.append(value)

                # Wave energy
                forecastTableRows = soup.find_all("tr", {"data-row-name":"energy"})
                for tableRow in forecastTableRows:
                        tableCells = tableRow.find_all('td', class_='forecast-table__cell')
                        for cell in tableCells:
                                value = cell.find("strong").text
                                energy.append(value)

                # TODO: Wind speed and direction
                forecastTableRows = soup.find_all("tr", {"data-row-name":"wind"})
                for tableRow in forecastTableRows:
                        print("\n Inicio ## \n")
                        tableCells = tableRow.find_all('div', class_='forecast-table__value')
                        # pra pegar a velo do vento usamos a tag <text>.text pra pegar o valor de dentro do text
                        for cell in tableCells:
                                wind_direction.append(cell.text)



                # TODO: Wave height is different (the nesting)
                """
                forecastTableRows = soup.find_all("tr", {"data-row-name":"wave-height"})
                for tableRow in forecastTableRows:
                        print("\n Inicio ## \n")
                        tableCells = tableRow.find_all('td', class_='forecast-table__cell')
                        for cell in tableCells:
                                value = cell.find("strong").text
                                print(value)
                                wave_height.append(value)
                """



                print("\nResultados:")
                print(len(energy))
                print(len(period))

                # When we parse the wind direction we get 'Vento' and 'km/h' as values, so we slice them out from the list!
                wind_direction = wind_direction[2:]
                print(wind_direction)
                print(len(wind_direction))


                #forecastTableCells = tableRow.find('td', class_='forecast-table__cell')
                #print(forecastTableCells, end='\n'*2)

                

                

# For debugging purposes without using Telegram's Bot
td = TideChecker()
td.checkContent()