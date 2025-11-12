'''Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként át
vett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! A program tartalmazza a függvény hívását is!'''

def osszegzo(szamok):
    sum_numbers = 0
    for num in szamok:
        sum_numbers = sum_numbers + num
    return sum_numbers

szamlista = [7,5,3,8,2]
szamok_osszege = osszegzo(szamlista)
print(f'A számok összege:{szamok_osszege}')