tetel_szam = int(input("Hány tétel legyen a nyugtán: "))
tetelek = []

ossz_ar = 0

for i in range(tetel_szam):
    jelenlegi_tetel = []
    tetel = input(f"{i + 1}. tétel: ")
    ar = input(f"{tetel} ára (Ft): ")
    while True:
        if ar.isdigit():

            jelenlegi_tetel.append(tetel)
            jelenlegi_tetel.append(ar)
            tetelek.append(jelenlegi_tetel)
            ossz_ar += int(ar)
            break
        else:
            print("Add meg az értékét egész számban!")
            ar = input(f"{tetel} ára (Ft): ")


def tetel(items):
    letter_amount = len(items[0])
    space = 20 - letter_amount

    print(items[0], '{:>{space}}'.format(items[1], space=space), "Ft")


def tetelsorok():
    for i in range(tetel_szam):
        tetel(tetelek[i])


szervdij = ossz_ar/10


def osszesit():
    for _ in range(24):
        print("=", end="")
    print()

    ossz_space = 20 - len("Összesen:")
    szerv_space = 19 - len("Szervízdíj:")

    print("Összesen:", '{:>{space}}'.format(ossz_ar, space=ossz_space), "Ft")
    print("Szervízdíj: ", '{:>{space}}'.format(szervdij, space=szerv_space), "Ft")

    for _ in range(24):
        print("=", end="")
    print()


def fizetendo():
    fiz_space = 20 - len("Fizetendő:")
    print("Fizetendő:", '{:>{space}}'.format(ossz_ar+szervdij, space=fiz_space), "Ft")


