import requests
import re
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
                        else:
                                print("Could not connect to the webpage.")
                except(ConnectionError):
                        print("Could not connect to the internet.")

        def checkContent(self):
                pageContent = self.response.content
                # Transform the page into a string so we can parse it
                pageText = self.response.text
                self.getContent(pageText)
                

        def getContent(self, pageText):
                soup = BS(pageText, "lxml")
                
                testao = soup.find('div', {'class' : "grafico_estado_actual_fondo"}).find('div', {'class' : "grafico_estado_actual_texto1"}).text
                # so ta pegando o primeiro resultado, queremos todos!
                testao2 = soup.find('div', {'class' : "grafico_estado_actual_fondo"}).find('div', {'class' : "grafico_estado_actual_texto1"}).find_all('span', {'class' : "rojo"})
                print(testao2)
                


                # Funciona
                primeiraPreiaMar = soup.find('div', {'class' : "grafico_estado_actual_fondo"}).find('div', {"id" : "grafico_estado_actual_texto_pleamar"}).text
                print(primeiraPreiaMar)
                primeiraBaixaMar = soup.find('div', {'class' : "grafico_estado_actual_fondo"}).find('div', {"id" : "grafico_estado_actual_texto_bajamar"}).text
                print(primeiraBaixaMar)

                # Nao Funciona, por que?
                """
                primeiroParsing = soup.find('div', {'class' : "grafico_estado_actual_fondo"})
                segundoParsing = primeiroParsing.find('div', {"id" : "grafico_estado_actual_texto_pleamar"}).text)
                print(segundoParsing)
                """
               
                
                

def run():
        TideChecker()

if __name__ == "__main__":
        run()