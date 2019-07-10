import requests

class TideChecker(object):
        def __init__(self):
                self.response = 0
                self.checkPage()

        def checkPage(self):
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

        def checkContent(self):
                pageContent = self.response.content
                #print(type(content))
                pageText = self.response.text
                print(pageText)
                print()


def run():
        TideChecker()

if __name__ == "__main__":
        run()