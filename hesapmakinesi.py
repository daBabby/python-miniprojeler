import os
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
                try:
                    num1 = int(input("1.Sayıyı giriniz:"))
                    num2 = int(input("2.Sayıyı giriniz:"))
                    sonuc = int(num1 + num2)
                    print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                except ValueError:
                    print("Lütfen doğru bir değer girin.")
                    input("Anamenüye dönmek için ENTER'a basınız")
            elif ıslem == "2":
                try:
                    num1 = int(input("1.Sayıyı giriniz:"))
                    num2 = int(input("2.Sayıyı giriniz:"))
                    sonuc = (num1 - num2)
                    print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                except ValueError:
                    print("Lütfen doğru bir değer giriniz.")
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
                except ValueError:
                    print("Lütfen doğru bir değer girin.")
                    input("Anamenüye dönmek için ENTER'a basınız")
            elif ıslem == "4":
                try:
                    num1 = int(input("1.Sayıyı giriniz:"))
                    num2 = int(input("2.Sayıyı giriniz:"))
                    sonuc = (num1 * num2)
                    print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                except ValueError:
                    print("Lütfen doğru bir değer girin.")
                    input("Anamenüye dönmek için ENTER'a basınız")
            elif ıslem == "5":
                try:
                    num1 = int(input("Tabanı giriniz: "))
                    num2 = int(input("Kuvetti giriniz:"))
                    sonuc = num1 ** num2
                    print("Seçtiğiniz işleme göre {} Taban {} üsttür".format(num1, num2))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                except ValueError:
                    print("Lütfen doğru bir değer girin.")
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
                try:

                    num1 = float(input("1.Sayıyı giriniz:"))
                    num2 = float(input("2.Sayıyı giriniz:"))
                    sonuc = float(num1 + num2)
                    print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                except ValueError:
                    print("Lütfen doğru bir değer girin.")
                    input("Anamenüye dönmek için ENTER'a basınız")
            elif ıslem == "2":
                try:
                    num1 = float(input("1.Sayıyı giriniz:"))
                    num2 = float(input("2.Sayıyı giriniz:"))
                    sonuc = (num1 - num2)
                    print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                except ValueError:
                    print("Lütfen doğru bir değer girin.")
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
                except ValueError:
                    print("Lütfen doğru bir değer girin.")
                    input("Anamenüye dönmek için ENTER'a basınız")
            elif ıslem == "4":
                try:
                    num1 = float(input("1.Sayıyı giriniz:"))
                    num2 = float(input("2.Sayıyı giriniz:"))
                    sonuc = (num1 * num2)
                    print("Seçtiğiniz işleme göre {} bu sayı ile {} bu sayının sonucu:".format(num1, num2, ))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                except ValueError:
                    print("Lütfen doğru bir değer girin.")
                    input("Anamenüye dönmek için ENTER'a basınız")
            elif ıslem == "5":
                try:
                    num1 = float(input("Tabanı giriniz: "))
                    num2 = float(input("Kuvetti giriniz:"))
                    sonuc = num1 ** num2
                    print("Seçtiğiniz işleme göre {} Taban {} üsttür".format(num1, num2))
                    print("=============================================================")
                    print("Sonuç:{}".format(sonuc))
                    print("=============================================================")
                    input("Anamenüye dönmek için ENTER'a basınız")
                except ValueError:
                    print("Lütfen doğru bir değer girin.")
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