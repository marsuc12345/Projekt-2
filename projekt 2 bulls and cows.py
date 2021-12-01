import random
import time


def vyhodnoceni(tip):
    tip = str(tip)
    list_tip = [tip[0], tip[1], tip[2], tip[3]]
    index = 0
    je_presne = 0
    je_mimo = 0
    for cislo in list_tip:
        if cislo == list_pocitac[index]:
            je_presne += 1
        elif cislo != list_pocitac[index] and cislo in list_pocitac:
            je_mimo += 1
        index += 1
    if je_presne == 1:
        print(je_presne, "Bull")
    else:
        print(je_presne, "Bulls")
    if je_mimo == 1:
        print(je_mimo, "Cow")
    else:
        print(je_mimo, "Cows")
    print(oddel_)


oddel_ = "-" * 37
oddel__ = "=" * 37
print(oddel__,"Vítej ve hře BULLS and COWS !".center(37),"Cílem hry je uhodnout 4 místné číslo.",
      "HODNĚ ŠTĚSTÍ VE HŘE !".center(37),oddel__,sep="\n")

pocitac = random.randrange(1000,9999)
while pocitac:
    cislice = str(pocitac)
    list_cislic = [cislice[0], cislice[1], cislice[2], cislice[3]]
    if cislice[0] != cislice[1] and cislice[0] != cislice[2] and cislice[0] != cislice[3] and \
            cislice[1] != cislice[2] and cislice[1] != cislice[3] and cislice[2] != cislice[3]:
        break
    else:
        pocitac = random.randrange(1000,9999)
pocitac = str(pocitac)
list_pocitac = [pocitac[0], pocitac[1], pocitac[2], pocitac[3]]

print("Vygenerováno číslo. Hádej...",oddel_,sep="\n")
start = time.time()
pocet_tipu = 1
pocet_chyb = 0

while True:
    tip = input()
    while tip:
        if len(tip) == 4 and str(tip[0]) != "0" and tip.isdigit() == 1 and str(tip[0]) != str(tip[1]) and \
                str(tip[0]) != str(tip[2]) and str(tip[0]) != str(tip[3]) and str(tip[1]) != str(tip[2]) and \
                str(tip[1]) != str(tip[3]) and str(tip[2]) != str(tip[3]):
            break
        else:
            print("Chybné zadání. Opakuj...",oddel_,sep="\n")
            pocet_chyb += 1
            tip = input()
    if tip != pocitac:
        vyhodnoceni(tip)
        pocet_tipu += 1
    elif tip == pocitac:
        end = time.time()
        vyhodnoceni(tip)
        print("*"*37,"!!! GRATULUJI K VÍTĚZSTVÍ !!!".center(37),"*"*37,sep="\n")
        print("- počet platných pokusů:",pocet_tipu,"x","\n- počet chybných zadání:",pocet_chyb,"x",
              "\n- hra trvala:",int(end - start),"s")
        break
