import requests


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
