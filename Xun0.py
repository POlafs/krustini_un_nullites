def zime_laukumu(vietas):
    Laukums = (f"|{vietas[1]}|{vietas[2]}|{vietas[3]}|\n"
            f"|{vietas[4]}|{vietas[5]}|{vietas[6]}|\n"
            f"|{vietas[7]}|{vietas[8]}|{vietas[9]}|")
    print(Laukums)

def parbauda_kartu(karta):
    if karta % 2 == 0:
        return '0'
    else:
        return 'X'

vietas = {
1: '1',
2: '2',
3: '3',
4: '4',
5: '5',
6: '6',
7: '7',
8: '8',
9: '9'
}
uzvar = 0
karta = 0
Spēle = 0

def parabauda_uzvara(vietas, uzvar):
    if (vietas[1] == vietas[2] == vietas[3]
or vietas[4] == vietas[5] == vietas[6]
or vietas[7] == vietas[8] == vietas[9]
or vietas[1] == vietas[4] == vietas[7]
or vietas[2] == vietas[5] == vietas[8]
or vietas[3] == vietas[6] == vietas[9]
or vietas[1] == vietas[5] == vietas[9]
or vietas[3] == vietas[5] == vietas[7]):
        uzvar = 1
    return uzvar
while Spēle == 0:
    if karta %2==0:
        print("1. spēlētāja kārta")
    else:
        print("2. spēlētāja kārta")
    zime_laukumu(vietas)
    izvele = input("Izvēlies vietu no (1-9) vai q, lai beigtu: ")
    if izvele == "q":
        print("Paldies par spēlēšanu!")
        Spēle += 1
    elif izvele.isdigit() and int(izvele) in vietas and vietas[int(izvele)] not in {"X","0"}:
        karta += 1
        vietas[int(izvele)] = parbauda_kartu(karta)
        uzvar = parabauda_uzvara(vietas, uzvar)
    if uzvar == 1:
        break
    if karta == 9 and uzvar == 0:
        print("Neizšķirts!")
        break
zime_laukumu(vietas)
if uzvar == 1:
    if parbauda_kartu(karta) == 'X':
        print("1. spēlētājs UZVAR!")
    else:
        print("2. spēlētājs UZVAR!")