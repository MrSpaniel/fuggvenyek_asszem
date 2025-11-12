'''Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként
átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza!
A program tartalmazza a függvény hívását is!
'''

def harommal_oszthatok(szamok):
    harommal = []
    for num in szamok:
        if num % 3 ==0:
            harommal.append(num)
    return len(harommal)
    


szamlista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]
hozzaadott = harommal_oszthatok(szamlista)
print(hozzaadott)