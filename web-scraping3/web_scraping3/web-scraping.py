import requests
from bs4 import BeautifulSoup
import re

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

    def kelime_ara(self, kelime):
        if self.soup:
          
            bulunan = self.soup.find_all(string=re.compile(re.escape(kelime), re.IGNORECASE))
            temizlenmis_metinler = [metin.strip() for metin in bulunan if metin.strip()]  
            return temizlenmis_metinler
        else:
            print("İçerik henüz yüklenmedi. Önce icerigi_getir() metodunu çağırın.")
            return []

url = "https://finans.mynet.com/kripto-para/"
kaziyici = KriptoKazıyıcı(url)
kaziyici.icerigi_getir()

kelime = input("Aramak istediğiniz kelimeyi girin: ")

sonuclar = kaziyici.kelime_ara(kelime)

if sonuclar:
    print("Arama sonuçları:")
    for sonuc in sonuclar:
        print(sonuc)
else:
    print(f"'{kelime}' kelimesi bulunamadı.")
