#Ödev: iç içe geçen for döngüsü ile 1, den 30'a kadar sayıların karelerini ve küplerini hsaplayan program yazınız
#Ödev2: While true döngüsü kullanılarak küçük bir hesap makinası yapınız...

#Ödev1
import time

for i in range(1,31):
    for j in range(1):
        print(f"İşlem için verilen değerler: {i}*{i} \nSonuç:",pow(i,2))
        print("-----------")
        print(f"İşlem için verilen değerler: {i}*{i}*{i} \nSonuç:",pow(i,3))
        print("**********")
#Ödev2
import time as t

print("Hesap makinesine hoş geldiniz")
while True:
    islem = input("Lütfen İşlem seçiniz: \n1-Toplama \n2-Çıkarma \n3-Çarpma \n4-Bölme \n(Çıkmak için q'yu tuşlayınız.)\nSeçiminiz: ")
    print("-------------")
    if islem=="1":
        print("Toplama İşlemi olarak işlem numarası seçilmiştir.")
        print(50 * "*")
        sayac_toplama = 1
        print("Yazmak istediğiniz tüm değerleri yazdıktan sonra '0' yazarak sonucu görebilirsiniz.")
        toplam = 0
        while True:
            toplama = float(input("Lütfen toplama işlemi için {}. sayıyı giriniz: ".format(sayac_toplama)))
            toplam += toplama
            sayac_toplama += 1
            if toplama == 0:
                print("Toplama işlemi sonucunuz:", toplam)
                print(50 * "-")
                break
    if islem=="2":
        print("Çıkarma İşlemi olarak işlem numarası seçilmiştir.")
        print(50 * "*")
        sayac_cikarma = 1
        print("Yazmak istediğiniz tüm değerleri yazdıktan sonra '0' yazarak sonucu görebilirsiniz.")
        cikarma = 0
        while True:
            cikarma = float(input("Lütfen çıkarma işlemi için {}. sayıyı giriniz: ".format(sayac_cikarma)))
            cikarma -= cikarma
            sayac_cikarma += 1
            if cikarma == 0:
                print("Çıkarma işlemi sonucunuz:", cikarma)
                print(50 * "-")
                break
    if islem=="3":
        print("Çarpma İşlemi olarak işlem numarası seçilmiştir.")
        print(50 * "*")
        sayac_carpma = 1
        print("Yazmak istediğiniz tüm değerleri yazdıktan sonra '0' yazarak sonucu görebilirsiniz.")
        carpma = 0
        while True:
            carpma = float(input("Lütfen çarpma işlemi için {}. sayıyı giriniz: ".format(sayac_carpma)))
            carpma *= carpma
            sayac_carpma += 1
            if carpma == 0:
                print("Çarpma işlemi sonucunuz:", carpma)
                print(50 * "-")
                break
    if islem=="4":
        print("Bölme İşlemi olarak işlem numarası seçilmiştir.")
        print(50 * "*")
        bolme1 = float(input("Lütfen Bölme işlemi için 1. sayıyı giriniz: "))
        bolme2 = float(input("Lütfen Bölme işlemi için 2. sayıyı giriniz: "))
        if bolme2 == 0:
            print(50 * "-")
            print("Payda 0 olduğu için bölme işlemi gerçekleşmez.")
        else:
            print("Bölme işlemi için girdiğiniz 1. sayı: ", bolme1, "\nBölme işlemi için girdiğiniz 2. sayı:", bolme2,
                  "\nBölümleri =", bolme1 / bolme2)
    if islem=="q":
        print("Hesap makinesinden çıkıyorsunuz...")
        t.sleep(1)
        break

