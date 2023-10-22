# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
# Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.

# Tvůj program bude obsahovat dvě funkce:
#       1/ První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (
#       pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. 
#       Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
# 
#       2/ Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
#       Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. 
#       Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí 
#       druhé funkce určí její cenu, kterou vypíše uživateli.

import math

cislo = input("Zadej telefonní číslo: ")
# jak ověřit délku, pokud by input byl integer? 

# overeni telefonniho cisla
def overeni_cisla(tel_cislo):
    """
    Ověří délku telefonního čísla, které zadá uživatel.
    Vrátí True nebo False podle odpovědi uživatele.
    """
    delka = len(tel_cislo)
    print(f"Počet znaků v telefonním čísle: {delka}.")
    povolena_delka1 = 9
    povolena_delka2 = 13
    if delka == povolena_delka1 or povolena_delka2:
        return True
    else:
        return False
    
verifikace = overeni_cisla(tel_cislo=cislo)
print(f"Výsledek je: {verifikace}.")

# v této části mi kód nefunguje, nehledě na zadaný počet znaků v telefonním číslo se automaticky dostane do větve True - můžu prosím nápovědu?

if verifikace == True:
    zprava_uzivatele = input("Zadej text SMS zprávy: ")    
else:
    print(f"Zadali jste nesprávné telefonní číslo.")
# pokud by zadal string namísto integer - v předchozím kroku elif
# else:
#     print(f"Nerozumím, začnete prosím znovu.")


# zadani SMS zpravy
pocet_znaku = 180
cena_SMS = 3

# zprava_uzivatele = input("Zadej text SMS zprávy: ")

def zprava (text):
    """
    Ověří počet znaků textu, který zadá uživatel.
    Podle odpovědi uživatele vrátí počet zpráv, do kterých bude text rozdělen a cenu v Kč za odeslání zprávy.
    """
    delka_zpravy = len(zprava_uzivatele)
    pocet_zprav = math.ceil(delka_zpravy/pocet_znaku)
    cena = pocet_zprav * cena_SMS
    print(f"Váš text bude odeslán v {pocet_zprav} SMS a cena odeslání je {cena} Kč.")

zprava(text=zprava_uzivatele)
