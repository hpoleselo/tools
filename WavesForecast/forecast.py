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
                wind_speed = []
                wind_state = []
                # TODO: usar dictionary pro wind e wind direction
                wind_direction = []
                high_tide = []
                low_tide = []

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

                # Wind speed and direction
                forecastTableRows = soup.find_all("tr", {"data-row-name":"wind"})
                for tableRow in forecastTableRows:
                        # Gets the wind direction
                        tableCells = tableRow.find_all('div', class_='forecast-table__value')
                        for cell in tableCells:
                                wind_direction.append(cell.text)

                        # Gets the wind speed
                        windSpeeds = tableRow.find_all('text', class_='wind-icon-val')
                        for windSpeed in windSpeeds:
                                # TODO: Check wind speed, i don't think they are right
                                wind_speed.append(windSpeed.text)


                # High-tide TODO: see how we separate the data retrieved (regarding the height AND sometimes we get 3 or 4 high and low tides..)
                # TODO: Are low tide and high tide always the same size? 46?
                forecastTableRows = soup.find_all("tr", {"data-row-name":"high-tide"})
                for tableRow in forecastTableRows:
                        tableCells = tableRow.find_all('div', class_='forecast-table__value--tiny')
                        for cell in tableCells:
                                high_tide.append(cell.text)

                # Low-tide
                forecastTableRows = soup.find_all("tr", {"data-row-name":"low-tide"})
                for tableRow in forecastTableRows:
                        lowTides = tableRow.find_all('div', class_='forecast-table__value--tiny')
                        for lowTide in lowTides:
                                low_tide.append(lowTide.text)


                # Wave height TODO: VER QUAL SWELL PEGAR, há 3 swells possiveis e ele ta confundindo na hora de pegar o swell!!!!
                # TODO: Arrumar a direcao
                forecastTableRows = soup.find_all("tr", {"data-row-name":"wave-height"})
                for tableRow in forecastTableRows:
                        swellDirections = tableRow.find_all('div', class_='forecast-table__value')
                        for swellDirection in swellDirections:
                                print(swellDirection.txt)

                        waveHeights = tableRow.find_all('text', class_='swell-icon-val')
                        for waveHeight in waveHeights:
                                wave_height.append(waveHeight.text)


                # TODO: Pegar dia da semana
                forecastTableRows = soup.find_all("tr", {"data-row-name":"days"})
                for tableRow in forecastTableRows:
                        swellDirections = tableRow.find_all('div', class_='data-day-name')
                        for swellDirection in swellDirections:
                                print(swellDirection.txt)


                # TODO: Pegar rating e escalar o melhor dia da semana como um resultado do boletim! Para isso precisariamos criar tipo uma tabela nossa
                # Onde essa tabela tem as datas e escolheriamos o indice da tabela usando pandas?



                print("\nResultados:")
                #print(wave_height)
                #print(len(wave_height))




                """
                print(high_tide)
                print(low_tide)
                print(len(low_tide))
                print(len(high_tide))
                """
                # When we parse the wind direction we get 'Vento' and 'km/h' as values, so we slice them out from the list!
                wind_direction = wind_direction[2:]

                

                

# For debugging purposes without using Telegram's Bot
td = TideChecker()
td.checkContent()