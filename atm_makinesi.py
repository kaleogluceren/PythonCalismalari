print("""
*******************************
ATM MAKİNESİNE HOŞGELDİNİZ...
İŞLEMLER;
1-BAKİYE SORGULAMA
2-PARA YATIRMA      
3-PARA ÇEKME

-Programdan Çıkmak İçin 'q' tuşuna basınız...
*******************************
""")
bakiye= 1000
while True:
    islem= input("işlemi seçiniz: ")

    if islem == "q":
        print("Çıkış Yapılıyor. Yine Bekleriz...")
        break
    elif islem == "1":
        print("Bakiyeniz {} tl'dir ".format(bakiye))

    elif islem == "2":
        miktar= int(input("Yatıracağınız Miktarı Giriniz: "))
        bakiye +=miktar

    elif islem == "3":
        miktar = int(input("Çekeceğiniz Miktarı Giriniz: "))
        if (bakiye - miktar < 0) :
            print("Böyle bir miktar çekemezsiniz")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz İşlem...")