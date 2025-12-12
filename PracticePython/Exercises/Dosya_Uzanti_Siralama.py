import os 
dosya_yolu = input("Dosya yolunu giriniz: \n")
os.chdir(dosya_yolu)  #chdir: çalışma dizinini girilen dosya_yolu na çevirir.Yani bundan sonra yapılacak işlemler bu klasörde gerçekleşir.
dosyalar = os.listdir(dosya_yolu) #dosya_yolu ' ndaki dosyaların listesi
uzantilar = []  #Boş bir liste tanımladık.Dosyaların uzantılarını buraya kaydedeceğiz.

for dosya in dosyalar:
    if os.path.isfile(dosya): #dosya mı değil mi diye kontrol ettik
        uzanti = dosya.split(".")[-1] #dosya adını . karakterinden böler. [-1] diyerek son parçayı alır. Bu da dosyanın uzantısını verir.
        if not uzanti in uzantilar:
            uzantilar.append(uzanti) #eğer bu uzantı daha önce listeye eklenmediyse listeye ekler.
        else:
            continue

for uzanti in uzantilar:  #eğer aynı isimde klasör varsa devam et yoksa yeni klasör oluştur.
    if os.path.isdir(uzanti):
        continue
    else:
        os.mkdir(uzanti)

for dosya in dosyalar: #dosya mı klasör mü?
    if os.path.isdir(dosya):
        continue
    else:
        uzanti = dosya.split(".")[-1] #dosyanın uzantısını alıyoruz.
        os.rename(os.path.join(dosya_yolu,dosya), os.path.join(dosya_yolu,dosya))