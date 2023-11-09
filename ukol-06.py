"""
Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:

Registrační značka	Značka a typ vozidla	Počet najetých kilometrů
4A2 3020	        Peugeot 403 Cabrio	    47534
1P3 4747	        Škoda Octavia	        41253

Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:

registrační značka automobilu registracni_znacka,
značka a typ vozidla typ_vozidla,
počet najetých kilometrů najete_km,
informaci o tom, jestli je vozidlo aktuálně volné dostupne (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).

Vytvoř metodu __init__() pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej 
jako parametry funkce __init__ a ulož je jako atributy objektu. 
Poslední atribut rovnou nastav jako True, tj. na začátku je vozidlo vždy volné.

Vytvoř objekty, které reprezentují oba automobily půjčovny.

Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. 
Funkce zkontroluje, jestli je vozidlo aktuálně volné. 
Pokud je volné, změní hodnotu atributu dostupne, který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". 
Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".

Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. 
Uživatel může zadávat hodnoty Peugeot nebo Škoda. 
Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto().

Otestuj, že program nedovolí půjčit stejné auto dvakrát.

"""

class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.stav = True

    def pujc_auto(self):
        if self.stav == True:
            self.stav = "dostupné"
            print(f"Potvrzuji zapůjčení vozidla.")
        else:
            self.stav = "půjčené"
            print(f"Vozidlo není k dispozici.")

    def get_info(self):
        return f"Informace o vozidle: {self.typ_vozidla}, registrační značky {self.registracni_znacka}, najeté km: {self.najete_km}."

Peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
Octavia = Auto("1P3 4747", "Škoda Octavia", 41253)

dotaz = input("O jaké vozidlo máte zájem?\n")
if dotaz == "Peugeot":
    print(Peugeot.get_info())
    Peugeot.pujc_auto()
elif dotaz == "Škoda":
    print(Octavia.get_info())
    Octavia.pujc_auto()
else:
    print(f"Omlouváme se, tento typ vozidla nepůjčujeme.")

dotaz2 = input("Máte zájem o zapůjčení dalšího vozidla?\n")

# Dá se vytvořit nějaký loop na dotaz? (Zápis níže není úplně to pravé ořechové.)
if dotaz2 == "Ano":
    dotaz3 = input("O jaké další vozidlo máte zájem?\n")
    if dotaz3 == "Peugeot":
        print(Peugeot.get_info())
        Peugeot.pujc_auto()
    elif dotaz3 == "Škoda":
        print(Octavia.get_info())
        Octavia.pujc_auto()
    else:
        print(f"Omlouváme se, tento typ vozidla nepůjčujeme.")
else:
    print(f"Těšíme se na Vaši další návštěvu.")
    exit()