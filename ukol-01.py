# ukol 1

name = "tereza"
domena = "@czechitas.cz"

e_mail = name + domena

print(e_mail)

# bonus
# Napiš program, který bude obsahovat proměnnou jmeno_a_prijmeni. 
# Obsah proměnné načti od uživatele pomocí funkce input. 
# Tvůj program postupně vypíše několik způsobů formátování jména.

jmeno_a_prijmeni = input("Zadej své jméno a příjmení: ")

#všechna písmena velká (vypíše např. JANA MALÁ)
print(jmeno_a_prijmeni.upper())

# všechna písmena malá (vypíše např. jana malá)
print(jmeno_a_prijmeni.lower())

# standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá) 
# nevím řešení

# iniciály (vypíše např. J. M.)
jmeno, prijmeni = jmeno_a_prijmeni.split(" ")
inicialy = jmeno[0] +"." + prijmeni[0] + "."
print(f"iniciály: {inicialy}")

# křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. 
# Jinak vypíše standardní variantu, tj. první písmeno velké, další malá 
# (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv) 
# nevím řešení