import random
import time
from os import system
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
                    print("Devam etmek için 'ENTER'A basınız")
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
            print("Devam etmek için 'ENTER'A basınız")
def cıkıs():
    print("İşlem sonlandırılıyor...")
    quit()
menu= """
[1] Taş-Kağıt-Makas oyna
[2] Yanındaki Arkadaşınla beraber Taş-Kağıt-Makas oyna
[Q] Çıkış
"""
while 1:
    while 1:
        print(menu)
        secim = input("Seçiminiz:")
        if secim == "1":
            oyunsolo()
        elif secim == "2":
            oyunduo()
        elif secim=="Q" or secim=="q":
            cıkıs()
        else:
            print("Lütfen doğru bir seçim yapın!")
