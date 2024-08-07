import requests
from bs4 import BeautifulSoup


class KriptoKazıyıcı:
    def __init__(self, url, basliklar=None):
        self.url = url
        self.basliklar = basliklar if basliklar else {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        }
        self.soup = None

    def icerigi_getir(self):
        try:
            yanit = requests.get(self.url, headers=self.basliklar)
            yanit.raise_for_status()  
            self.soup = BeautifulSoup(yanit.content, "html.parser")
        except requests.exceptions.RequestException as e:
            print(f"{self.url} adresinden içerik getirilemedi: {e}")
            self.soup = None