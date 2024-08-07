from bs4 import BeautifulSoup
import re

def kelime_ara(self, kelime):
        if self.soup:
          
            bulunan = self.soup.find_all(string=re.compile(re.escape(kelime), re.IGNORECASE))
            temizlenmis_metinler = [metin.strip() for metin in bulunan if metin.strip()]  
            return temizlenmis_metinler
        else:
            print("İçerik henüz yüklenmedi. Önce icerigi_getir() metodunu çağırın.")
            return []
