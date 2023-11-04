# Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.

# Soubor si ulož a načti do slovníku.

# Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). 
# Vytvoř nový slovník. 
# Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. 
# Pokud má méně než 60, hodnota bude "Fail".

# Výsledný slovník ulož jako JSON do souboru prospech.json.


import json

with open("body.json", mode = "r", encoding="utf-8") as file: 
    body = json.load(file) 

# prazdny slovnik
PassOrFail = {}

for klic in body: 
    # print(key)
    vysledek = ""
    skore = body[klic]
    if skore >= 60:
        vysledek = "Pass"
    else:
        vysledek = "Fail" 
    PassOrFail[klic] = vysledek 

print(PassOrFail)

# zlepšení od Liuby
PassOrFail2 = {}

for klic, skore in body.items():
    if skore >= 60:
        vysledek = "Pass"
    else:
        vysledek = "Fail" 
    PassOrFail2[klic] = vysledek

print(PassOrFail2)

with open("prospech.json", mode="w", encoding="utf-8") as file:
    json.dump(PassOrFail, file, ensure_ascii=False, indent=4)

with open("prospech.json", mode="w", encoding="utf-8") as file:
    json.dump(PassOrFail2, file, ensure_ascii=False, indent=4)