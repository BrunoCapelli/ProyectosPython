
#  Ejercicio 3
"""
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
últimas tiene que decir que riman un poco y si no, que no riman.
"""

primer_cadena = input("Ingrese la primer palabra: ")
segunda_cadena = input("Ingrese la segunda palabra: ")
lista1 = []
lista2 = []
contador = 0
for letra in primer_cadena:
    lista1.append(letra)
for letra in segunda_cadena:
    lista2.append(letra)

ultimas_letras1 = list(lista1[-3:])
ultimas_letras2 = list(lista2[-3:])

for indice in range (0,3):
    if ultimas_letras1[indice] == ultimas_letras2[indice]:
        contador += 1

if contador == 3:
    print("Las palabras riman!")
elif contador == 2:
    print("Las palabras riman un poco")
else:
    print("No rima")
