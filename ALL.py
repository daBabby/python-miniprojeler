import random
import os
import time
def geometri():
    def geometri(sekil):
        while 1:
            if len(sekil) == 3:
                a = sekil[0]
                b = sekil[1]
                c = sekil[2]

                if (a == b) and (a == c) and (c == b):
                    print("Eşkenar üçgen")
                    print("-"*15)
                    break
                elif a == b or a == c or b == c:
                    print("İkizkenar")
                    break
                else:
                    print("Çesitkenar üçgen")
                    breake
            elif len(sekil) == 4:
                a = sekil[0]
                b = sekil[1]
                c = sekil[2]
                d = sekil[3]

                if (a == b) and (a == c) and (a == d):
                    print("KARE")
                elif (a == b) and (c == d):
                    print("Dikdörtgen")
                else:
                    print("Normal dörtgen")
            else:
                print("Lütfen doğru bir değer giriniz!")
    while (True):
        try:
            elemansayısı = int(input("Elamanları Sayısını girin:"))
            if (elemansayısı == 3):
                a = int(input("A:"))
                b = int(input("B:"))
                c = int(input("C:"))
                geometri([a, b, c])
            if (elemansayısı == 4):
                a = int(input("A:"))
                b = int(input("B:"))
                c = int(input("C:"))
                d = int(input("D:"))
                geometri([a, b, c, d])
            else:
                print("tekrar giriniz")
        except ValueError:
            print("Lütfen doğru bir değer giriniz!")
def hesap():
    while (True):
        os.system("cls")
        try:
            print("--------------------------------------------------------")
            print("-           Hesap makinesine Hoşgeldiniz.              -")
            print("--------------------------------------------------------")

            print("[1] Tam sayı işlemler")
            print("[2] Ondalık sayı işlemleri")
            print("[Q] Çıkış")
            secenek1 = (input("Lütfen nasıl bir işlem yapmak istediğinizi seçiniz: "))
            if secenek1 == "1":
                print("--------------------------------------------------------")
                print("-       Tam sayı işlemlerindesiniz.                    -")
                print("--------------------------------------------------------")
                print("""
                [1] Toplama
                [2] Çıkarma
                [3] Bölme
                [4] Çarpma   
                [5] Üst alma
                [Q] Çıkış
                """)

                ıslem = (input("Hangi işlemi yapmak istiyorsunuz: "))
                if ıslem == "1":
                    num1 = int(input("1.Sayıyı giriniz:"))
                    num2 = int(input("2.Sayıyı giriniz:"))
                    sonuc = int(num1 + num2)
                    print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                elif ıslem == "2":
                    num1 = int(input("1.Sayıyı giriniz:"))
                    num2 = int(input("2.Sayıyı giriniz:"))
                    sonuc = (num1 - num2)
                    print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                elif ıslem == "3":
                    try:
                        num1 = int(input("1.Sayıyı giriniz:"))
                        num2 = int(input("2.Sayıyı giriniz:"))
                        sonuc = int(num1 / num2)
                        print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                        print("=============================================================")
                        print("Sonuç:{}".format(sonuc))
                        print("=============================================================")
                        input("Anamenüye dönmek için ENTER'a basınız")
                    except ZeroDivisionError:
                        print("=============================================================")
                        print("Tanımsız")
                        print("=============================================================")
                        input("Anamenüye dönmek için ENTER'a basınız")
                elif ıslem == "4":
                    num1 = int(input("1.Sayıyı giriniz:"))
                    num2 = int(input("2.Sayıyı giriniz:"))
                    sonuc = (num1 * num2)
                    print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                elif ıslem == "5":
                    num1 = int(input("Tabanı giriniz: "))
                    num2 = int(input("Kuvetti giriniz:"))
                    sonuc = num1 ** num2
                    print("Seçtiğiniz işleme göre {} Taban {} üsttür".format(num1, num2))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                elif (ıslem == "Q") or (ıslem == "q"):
                    print("işlem sonlandırılıyor")
                    break
                else:
                    print("Hatalı giriş seçeneği Lütfen düzgün giriniz.")
            elif secenek1 == "2":
                print("--------------------------------------------------------")
                print("-     Ondalık sayı işlemlerindesiniz.                  -")
                print("--------------------------------------------------------")
                print("""
                    [1] Toplama
                    [2] Çıkarma
                    [3] Bölme
                    [4] Çarpma
                    [5] Üst alma
                    [Q] Çıkış
                    """)
                ıslem = (input("Hangi işlemi yapmak istiyorsunuz: "))
                if ıslem == "1":
                    num1 = float(input("1.Sayıyı giriniz:"))
                    num2 = float(input("2.Sayıyı giriniz:"))
                    sonuc = float(num1 + num2)
                    print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                elif ıslem == "2":
                    num1 = float(input("1.Sayıyı giriniz:"))
                    num2 = float(input("2.Sayıyı giriniz:"))
                    sonuc = (num1 - num2)
                    print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                elif ıslem == "3":
                    try:
                        num1 = float(input("1.Sayıyı giriniz:"))
                        num2 = float(input("2.Sayıyı giriniz:"))
                        sonuc = float(num1 / num2)
                        print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                        print("=============================================================")
                        print("Sonuç:{}".format(sonuc))
                        print("=============================================================")
                        input("Anamenüye dönmek için ENTER'a basınız")
                    except ZeroDivisionError:
                        print("=============================================================")
                        print("Tanımsız")
                        print("=============================================================")
                        input("Anamenüye dönmek için ENTER'a basınız")
                elif ıslem == "4":
                    num1 = float(input("1.Sayıyı giriniz:"))
                    num2 = float(input("2.Sayıyı giriniz:"))
                    sonuc = (num1 * num2)
                    print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                elif ıslem == "5":
                    num1 = float(input("Tabanı giriniz: "))
                    num2 = float(input("Kuvetti giriniz:"))
                    sonuc = num1 ** num2
                    print("Seçtiğiniz işleme göre {} Taban {} üsttür".format(num1, num2))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                elif ıslem == "Q" or ıslem == "q":
                    print("İşlem sonlandırıldı.")
                    break
                else:
                    print("Hatalı giriş seçeneği Lütfen düzgün giriniz.")
            elif secenek1 == "q" or secenek1 == "Q":
                print("İşlem sonlandırıldı.")
                break
            else:
                print("Yanlış bir seçenek seçtiniz lütfen tekrar deneyiniz.")
        except ZeroDivisionError:
            print("Lütfen doğru bir değer gir")
def oyunduo():
    menu = """
            [1] Manuel oyna
            [2] Random oyna
            [Q] Çıkış
            """
    while 1:
        print(menu)
        secim = input("Lütfen hangi işlemi yapacağınızı seçin:")
        if secim=="1":
            l = ['Taş', 'Kağıt', 'Makas']
            def sonuc():
                if (i == "Makas" or i == "makas") and (b == "Makas" or b == "makas"):
                    print("Berabere!")
                elif (i == "Kağıt" or i == "kağıt") and (b == "Kağıt" or b == "kağıt"):
                    print("Berabere")
                elif (i == "Taş" or i == "taş") and (b == "Taş" or b == "taş"):
                    print("Berabere")
                elif (i == "Taş" or i == "taş") and (b == "Kağıt" or b == "kağıt"):
                    print("{} Kazandı!".format(c))                 #c=b m=i
                elif (i == "Taş" or i == "taş") and (b == "Makas" or b == "makas"):
                    print("{} Kazandı!".format(m))
                elif (i == "Makas" or i == "makas") and (b == "Taş" or b == "taş"):
                    print("{} Kazandı!".format(c))
                elif (i == "Makas" or i == "makas") and (b == "Kağıt" or b == "kağıt"):
                    print("{} Kazandı!".format(m))
                elif (i == "Kağıt" or i == "kağıt") and (b == "Taş" or b == "taş"):
                    print("{} Kazandı!".format(m))
                elif (i == "Kağıt" or i == "kağıt") and (b == "Makas" or b == "makas"):
                    print("{} Kazandı!".format(c))                                                     #c=b m=i
                else:
                    print("Hatalı giriş yaptınız lütfen tekrar deneyiniz")
            c = input('Birinci oyuncunun adı: ')
            m = input('İkinci oyuncunun adı: ')
            while 1:
                time.sleep(0.4)
                b = input("Hangi Hareketi yapmak istiyorsun? {}".format(c))
                os.system("cls")
                time.sleep(0.4)
                i = input("Hangi hareketi yapmak istiyorsun? {} ".format(m))
                print("-" * 15)
                print("{}=".format(c), b)
                print("-" * 15)
                print('{}='.format(m), i)
                print("=" * 15)
                sonuc()
                print("=" * 15)
                x = input("Lütfen devam etmek için 'enter'a,Çıkış yapmak için 'Q'ye basın")
                if x in ['Q', 'q']:
                    break
        elif secim=="2":
            l = ['Taş', 'Kağıt', 'Makas']

            def sonuc():
                if b == i:
                    print('Berabere')
                elif (b == 'Taş') and (i == 'Kağıt'):
                    print('{} kazandı.'.format(c))
                elif (b == 'Taş') and (i == 'Makas'):
                    print('{} kazandı.'.format(c))
                elif (b == 'Kağıt') and (i == 'Taş'):
                    print('{} kazandı.'.format(c))
                elif (b == 'Kağıt') and (i == 'Makas'):
                    print('{} kazandı.'.format(m))
                elif (b == 'Makas') and (i == 'Taş'):
                    print('{} kazandı.'.format(m))
                else:
                    print('{} kazandı.'.format(c))

            c = input('Birinci oyuncunun adı: ')
            m = input('İkinci oyuncunun adı: ')
            while 1:
                time.sleep(0.4)
                b = random.choice(l)
                time.sleep(0.4)
                i = random.choice(l)
                print("-" * 15)
                print("{}=".format(c), b)
                print("-" * 15)
                print('{}='.format(m), i)
                print("=" * 15)
                sonuc()
                print("=" * 15)
                x = input("Lütfen devam etmek için 'enter'a,Çıkış yapmak için 'Q'ye basın")
                if x in ['Q', 'q']:
                    break
        elif secim=="q" or secim=="Q":
            print("İşlem sonlandırılıyor...")
            break
    else:
        print("Lütfen doğru bir işlem yapın")
def oyunsolo():
    while True:
        l = ['Taş', 'Kağıt', 'Makas']
        i = input("Hangi Haraketi yapmak istiyorsunuz:")
        if i=="q" or i =="Q":
            print("İşlem sonlandırılıyor...")
            break
        input("Lütfen devam etmek için 'enter'a basın")
        print("=" * 25)
        b = random.choice(l)
        print("Seçiminiz: {}".format(i))
        print("Rakibin: {}".format(b))
        if (i == "Makas" or i == "makas") and (b == "Makas" or b == "makas"):
            print("Berabere!")
        elif (i == "Kağıt" or i == "kağıt") and (b == "Kağıt" or b == "kağıt"):
            print("Berabere")
        elif (i == "Taş" or i == "taş") and (b == "Taş" or b == "taş"):
            print("Berabere")
        elif (i == "Taş" or i == "taş") and (b == "Kağıt" or b == "kağıt"):
            print("Sen Kaybettin!")
        elif (i == "Taş" or i == "taş") and (b == "Makas" or b == "makas"):
            print("Sen Kazandın!")
        elif (i == "Makas" or i == "makas") and (b == "Taş" or b == "taş"):
            print("Sen Kaybettin!")
        elif (i == "Makas" or i == "makas") and (b == "Kağıt" or b == "kağıt"):
            print("Sen kazandın!")
        elif (i == "Kağıt" or i == "kağıt") and (b == "Taş" or b == "taş"):
            print("Sen Kazandın!")
        elif (i == "Kağıt" or i == "kağıt") and (b == "Makas" or b == "makas"):
            print("Sen Kaybettin!")
        else:
            print("Hatalı giriş yaptınız lütfen tekrar deneyiniz")
def cıkıs():
    print("İşlem sonlandırılıyor...")
    quit()
def zar():
    """
    2 adet zar atılsın ve 2 zarın toplamı ekrana yazılsın monopoli gibi oynayanlar için bir
    program olsun
    """
    menu = """
    [1] Oyuna başla
    [Q] Çıkış
    """
    menu2 = """
    [1] Zar at
    [2] 6,6 Gelene kadar Zar at
    [Q] Çıkış
    """
    def oyun6():
        i = 1
        while True:
            zar_1 = random.randint(1, 6)
            zar_2 = random.randint(1, 6)
            if zar_1 == 6 and zar_2 == 6:
                print("Deneme {}:\t({},{}) *** ".format(i, zar_1, zar_2))
                time.sleep(1)
                print(" ")
                print("\n** {}. denemede (6,6) geldi **".format(i))
                x = input("Lütfen tekrar oynamak için 'R' çıkmak için 'Q'ye basın")
                if x == "Q" or x == "q":
                    break
                elif x == "r" or x == "R":
                    oyun6()
                else:
                    print("Lütfen düzgünn işlem yapınız")

            i += 1
            time.sleep(0.5)

        print("\n** {}. denemede (6,6) geldi **".format(i))
    def oyun():
        while True:
            zar_1 = random.randint(1, 6)
            zar_2 = random.randint(1, 6)
            if zar_1 == zar_2:
                toplam = zar_1 + zar_2
                print("Düşeş attınız!**{}**:({},{}) ".format(toplam, zar_1, zar_2))
                time.sleep(0.2)
                x = input("Lütfen devam etmek için 'ENTER' çıkmak için 'Q'ye basın")
                if x == "Q" or x == "q":
                    break
            elif zar_1 != zar_2:
                toplam = zar_1 + zar_2
                print("Atığınız Sayı:**{}**({},{})".format(toplam, zar_1, zar_2))
                time.sleep(0.5)
                x = input("Lütfen devam etmek için 'ENTER' çıkmak için 'Q'ye basın")
                if x == "Q" or x == "q":
                    break
            else:
                print("Lütfen geçerli bir işlem yapın!")
    while 1:
        print(menu)
        secim = input("Seçiminiz:")
        if secim == "1":
            print(menu2)
            secim2 = input("Seçiminiz")
            if secim2 == "1":
                oyun()
            elif secim2 == "2":
                oyun6()
            elif secim2 == "Q" or secim2 == "q":
                print("İşlem sonlandırılıyor...")
                break
        elif secim == "Q" or secim == "q":
            print("İşlem sonlandırılıyor...")
            break
menu= """
[1] Taş-Kağıt-Makas oyna
[2] Arkadaşınla beraber Taş-Kağıt-Makas oyna
[3] Hesap Makinesi
[4] Geometrik şekil(Kare-Diktörtgen-İkizkenar-Çeşitkenar-Eşkenar)
[5] Zar Atma Oyna
[Q] Çıkış
"""
while 1:
    print(menu)
    secim =input("Seçiminiz:")
    if secim=="1":
        oyunsolo()
    elif secim=="2":
        oyunduo()
    elif secim  == "3":
        hesap()
    elif secim=="4":
        geometri()
    elif secim=="5":
        zar()
    elif secim =="Q" or secim=="q":
        cıkıs()
    else:
        print("Hatalı giriş yaptınız lütfen tekrar deneyiniz!")