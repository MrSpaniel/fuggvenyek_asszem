'''Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett 
listaelemek (egész számok) között van páros,
ellenkező esetben a visszatérési érték False! A program tartalmazza a függvény hívását is!'''

def paros_e(egesz_szamok):
    for szam in egesz_szamok:
        if szam % 2 ==0:
            x = True
            break
        else:
            x = False
    return x


szamlista = [1, 3, 4, 5, 6, 7]
valasz = paros_e(szamlista)
print(valasz)