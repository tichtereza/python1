"""
Mějme zadaný následující seznam naměřených teplot. 
Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

"""
import math
import statistics

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]


# a/ Vytvoř seznam průměrných teplot pro každý den.

denni_prumer = []

for den in teploty:
    average = round(statistics.mean(den), 2)
    # print(average)
    denni_prumer.append(average)

print(denni_prumer)

# a/ zápis pomocí List Comprehension
denni_prumerne_teploty = [round(statistics.mean(den),2) for den in teploty]
print(denni_prumerne_teploty)

# b/ Vytvoř seznam ranních teplot.
ranni_teploty = []

for den in teploty:
    ranni_teplota = den[0]
    ranni_teploty.append(ranni_teplota)

print(ranni_teploty)

# c/ Vytvoř seznam nočních teplot.

nocni_teploty = [den[3] for den in teploty]
print(nocni_teploty)

# d/ Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.

poledni_a_nocni_teploty = []

for den in teploty:
    poledne_a_noc = [den[1], den[-1]]
    poledni_a_nocni_teploty.append(poledne_a_noc)

print(poledni_a_nocni_teploty)