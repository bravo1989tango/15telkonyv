class telkonyv():
    def __init__(self, veznev, keresztnev, telszam, leiras):
        self.veznev = veznev
        self.keresztnev = keresztnev
        self.telszam = telszam
        self.leiras = leiras

    def teljesnev(self):
        vez_kereszt = self.veznev + " " + self.keresztnev
        return vez_kereszt

def update(telefonkonyv):
    eredeti = input("Régi név: ")
    ujnev1 = input("Új vezeték: ")
    ujnev2 = input("Új kereszt: ")
    szam = telszam()
    for telkonyv in telefonkonyv:
        if eredeti == telkonyv.teljesnev():
            telkonyv.veznev = ujnev1
            telkonyv.keresztnev = ujnev2
            telkonyv.telszam = szam
            print(telkonyv.teljesnev() + " " + telkonyv.telszam + "\n")
            break
    for telkonyv in telefonkonyv:
        print(telkonyv.teljesnev() + " " + telkonyv.telszam)

def lista():
    return int(input("1,olvasás\n2,irás\n3,kilépés\n"))

def bevitel():
    while True:
        try:
            return lista()
        except ValueError:
            print("Érvénytelen bevitel!")

def telszam():
    szam = input("Kérem a számot: ")
    try:
        if szam[0] == "+":
            int(szam[1:])
            return szam
        int(szam)
        return szam
    except ValueError:
        print("Próbáld újra: +36301234567")

def nevkiiras(telefonkonyv):
    for telkonyv in telefonkonyv:
        print(telkonyv.teljesnev())
    adat = input("Kérem a nevet: ")
    for telkonyv in telefonkonyv:
        if adat == telkonyv.teljesnev():
            print("Van ilyen név a könyvben, ez a száma: " + telkonyv.telszam + "\n")
            break


def main():
    telefonkonyv = [telkonyv("Alfa", "Aladár", "+36701234567", "Hülye"), telkonyv("Béta", "Béla", "+36309876543", "Okos"), telkonyv("Gamma", "Gábor", "+36309872343", "Sugárzó")]
    akcio = bevitel()
    while True:
        if akcio == 1:
            nevkiiras(telefonkonyv)
        elif akcio == 2:
            update(telefonkonyv)
        elif akcio == 3:
            break

main()