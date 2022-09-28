print("""***************
HESAP MAKİNESİ

1. TOPLAMA İŞLEMİ 

2. ÇIKARMA İŞLEMİ

3. ÇARPMA İŞLEMİ 

4. BÖLME İŞLEMİ 

************************
""")

a=int(input("Birinci sayıyı giriniz: "))
b=int(input("İkinci sayıyı giriniz: "))
islem=input("İşlemi Giriniz: ")

if islem == "1":
    print("{} ile {}'nın toplamı {}'dır".format(a,b,a+b))

elif islem == "2":
    print("{} ile {}'nın Farkı {}'dır".format(a,b,a-b))

elif islem == "3":
    print("{} ile {}'nın Çarpımı {}'dır".format(a,b,a*b))

elif islem == "4":
    print("{} ile {}'nın Bölümü {}'dır".format(a,b,a/b))

else:
    print("Geçersiz İşlem Girdiniz.....")