def geometri():
    def geometri(sekil):
        while 1:
            if len(sekil) == 3:
                a = sekil[0]
                b = sekil[1]
                c = sekil[2]

                if (a == b) and (a == c) and (c == b):
                    print("-" * 15)
                    print("Eşkenar üçgen")
                    print("-" * 15)
                    break
                elif (a == b) or (a == c) or (b == c):
                    print("-" * 15)
                    print("İkizkenar")
                    print("-" * 15)
                    break
                else:
                    print("-" * 15)
                    print("Çesitkenar üçgen")
                    print("-" * 15)
                    break
            elif len(sekil) == 4:
                a = sekil[0]
                b = sekil[1]
                c = sekil[2]
                d = sekil[3]

                if (a == b) and (a == c) and (a == d):
                    print("-" * 15)
                    print("KARE")
                    print("-" * 15)
                    break
                elif (a == b) and (c == d):
                    print("-" * 15)
                    print("Dikdörtgen")
                    print("-" * 15)
                    break
                else:
                    print("-" * 15)
                    print("Normal dörtgen")
                    print("-" * 15)
                    break
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

        except ValueError:
            print("Lütfen doğru bir değer giriniz!")
geometri()