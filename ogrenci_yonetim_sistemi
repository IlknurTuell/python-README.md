ogrenciler = {}
bolumler = set()

# Öğrenci ekleme fonksiyonu
def ogrenci_ekle():
    print("\n---ÖĞRENCİ EKLEME---")

    isim = input("Öğrenci adı ve soyadı: ")
    bolum = input("Öğrenci bölümü: ")

    ogrenci_id = "ogrenci" + str(len(ogrenciler)+1)
    bilgi = (isim,bolum)
    notlar = []
    ogrenciler[ogrenci_id] = {"bilgi": bilgi, "notlar": notlar}
    bolumler.add(bolum)

    print(f"2{ogrenci_id} sisteme başarıyla eklendi.")

# Öğrenci listeleme fonksiyonu 
def ogrenci_listele():
    print("\n---ÖĞRENCİ LİSTESİ---")
    if not ogrenciler:
        print("Henüz kayıtlı öğrenci yok.")
    else:
        for ogrenci_id , bilgiler in ogrenciler.items():
            isim , bolum = bilgiler["bilgi"]
            notlar = bilgiler["notlar"]
            print(f"\nID: {ogrenci_id}")
            print(f"Ad Soyad: {isim}")
            print(f"Bölüm: {bolum}")
            print(f"Notlar: {notlar if notlar else 'Not yok'}")

# Not ekleme fonksiyonu
def not_ekle():
    print("\n---NOT EKLEME---")
    ogrenci_id = input("Not eklenecek öğrenci ID:")
    if ogrenci_id in ogrenciler:
        try:
            yeni_not = int(input("Notu girin: "))
            ogrenciler[ogrenci_id]["notlar"].append(yeni_not)
            print("Not başarıyla eklendi.")
        except ValueError:
            print("Lütfen sayı giriniz.")
    else:
        print("Öğrenci bulunamadı.")

# Ortalama hesaplama fonksiyonu
def ortalama_hesapla():
    print("\n---ORTALAMA HESAPLAMA---")
    ogrenci_id = input("Ortalaması hesaplanacak öğrenci ID:")
    if ogrenci_id in ogrenciler:
        notlar = ogrenciler[ogrenci_id]["notlar"]
        if notlar:
            ort = sum(notlar) / len(notlar)
            print(f"{ogrenci_id} ortalaması : {ort: .2f}")
        else:
            print("Bu öğrenci için not girilmemiş.")
    else:
        print("Öğrenci bulunamadı.")


# Öğrenci silme fonksiyonu
def ogrenci_sil():
    print("\n---ÖĞRENCİ SİLME---")
    ogrenci_id = input("Silmek istediğiniz öğrenci ID:")
    if ogrenci_id in ogrenciler:
        isim = ogrenciler[ogrenci_id]["bilgi"][0]
        ogrenciler.pop(ogrenci_id)
        print(f"{isim} başarıyla silindi.")
    else:
        print("Böyle bir öğrenci bulunamadı.")

# Bölümleri listeleme fonksiyonu
def bolumleri_göster():
    print("\n---KAYITLI BÖLÜMLER---")
    if bolumler:
        for bolum in bolumler:
            print(f"- {bolum}")
    else:
        print("Henüz bölüm eklenmemiş.")

# Menü sistemi fonksiyonu
def menu():
    while True:
        print("\n*****ÖĞRENCİ YÖNETİM SİSTEMİ*****")
        print("1 - Öğrenci ekle")
        print("2 - Öğrenci listele")
        print("3 - Not ekle")
        print("4 - Ortalama hesapla")
        print("5 - Öğrenci sil")
        print("6 - Bölümleri göster")
        print("0 - Çıkış")

        secim = input("Seçiniz: ")
        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            ogrenci_listele()
        elif secim == "3":
            not_ekle()
        elif secim == "4":
            ortalama_hesapla()
        elif secim == "5":
            ogrenci_sil()
        elif secim == "6":
            bolumleri_göster()
        elif secim == "0":
            print("Program sonlandırılıyor.")
            break
        else:
            print("Geçersiz işlem.")

menu()
