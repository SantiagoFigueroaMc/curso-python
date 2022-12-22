"""
Similar al ciclo while, el ciclo for sirve para repetir código según una condición
"""

amigos = [
    "Pedro",
    "Juan",
    "Diego",
    "Trini",
    "Berni",
    "Cata"
]

# 'for' es una palabra reservada (al igual que 'in')
# luego de for se puede declarar el tipo de condición para el ciclo
# ejemplo: 'amigo' es una variable que cambiará con cada ciclo
#   el ciclo irá asignando los valores de la lista 'amigos'
for amigo in amigos:
    print(amigo)