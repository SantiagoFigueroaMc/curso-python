"""
Funciones
"""

# Esta es una función
# def es una palabra especial para declarar una función
# 'sumar' es el nombre de la función, se usa luego para invocarla
# a y b son parámetros de la función, son variables que solo existen dentro de la función
# return indica el final de la función, puede haber más de un return
def sumar(a, b):
    return a + b

# Uso de las funciones:
x = 1
y = 5
resultado = sumar(x, y)

print("Sumando", x, "con", y)
print(resultado)