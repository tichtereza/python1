# Vyvíjíš software pro obchod s elektronickými součástkami. 
# Firma eviduje informace o počtu součástek na skladě ve slovníku. 
# Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

# Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník. 
# Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. Obě informace si ulož. 
# Následně naprogramuj následující varianty:

# sklad = {
#   "1N4148": 250,
#   "BAV21": 54,
#   "KC147": 147,
#   "2N7002": 97,
#   "BC547C": 10
# }

# a) Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
# b) Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, 
# vypiš text o tom, že lze prodat pouze omezené množství kusů. 
# Následně součástku odeber ze slovníku, protože je vyprodaná.
# c) Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, 
# že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.


sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

soucastka = input("Zadejte kód součástky: ")

if soucastka in sklad:
    mnozstvi = int(input("Zadejte požadované množství součástky: "))
    pocet = sklad[soucastka]
    if pocet >= mnozstvi:
        print(f"Součástka {soucastka} je skladem v požadovaném množství {mnozstvi} ks.")
        pocet = pocet - mnozstvi
        sklad[soucastka] = pocet
        print(f"Na skladě nyní zbývá {pocet} ks součástky {soucastka}. Dostupné součástky skladem: {sklad}.")
    else:
        print(f"Skladová zásoba součástky {soucastka} je pouze: {pocet} ks. Položka je nyní vyprodána.")
        vyprodano = sklad.pop(soucastka)
        print(f"Dostupné součástky skladem: {sklad}.")
else:
    print(f"Součástka s tímto kódem není skladem.")
