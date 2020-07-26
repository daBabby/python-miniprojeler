import random
import time
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
            print("""Deneme {}:\t({},{}) """.format(i, zar_1, zar_2))
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
zar()