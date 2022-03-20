
#   Ejercicio 2
"""
Escribe un programa que te permita jugar a una versión simplificada del
juego Master Mind. El juego consistirá en adivinar una cadena de números
distintos. Al principio, el programa debe pedir la longitud de la cadena (de 2
a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la
cadena de números. En cada intento, el programa informará de cuántos números
han sido acertados (el programa considerará que se ha acertado un número si
coincide el valor y la posición).
"""
from ast import If
import random


largo_cadena = int(input("Ingrese el largo de la cadena: "))
while (largo_cadena < 2) or (largo_cadena > 9):
        print("El largo de la cadena debe ser entre 2 y 9")
        largo_cadena = int(input("Ingrese el largo de la cadena: "))
def nro_aleatorio():
    global var
    if (largo_cadena < 2) or (largo_cadena > 9):
        print("El largo de la cadena debe ser entre 2 y 9")
    if largo_cadena == 2:
        var = (random.randint(10, 99))
    if largo_cadena == 3:
        var = (random.randint(100, 999))
    if largo_cadena == 4:
        var = (random.randint(1000, 9999))
    if largo_cadena == 5:
        var= (random.randint(10000, 99999))
    if largo_cadena == 6:
        var = (random.randint(100000, 999999))
    if largo_cadena == 7:
        var = (random.randint(1000000, 9999999))
    if largo_cadena == 8:
        var = (random.randint(10000000, 99999999)) 
    if largo_cadena == 9:
        var = (random.randint(100000000, 999999999))   
    return  var


nro_aleatorio()
nro_random = str(var)
#print(nro_random)           # Numero aleatorio
lista = []
#print(len(lista))

def aproximar_cadena(var):
    contadorCifrasCorrectas = 0
    fin = False
    for num in nro_random:
        lista.append(num)
    while fin == False:
        contadorCifrasCorrectas = 0
        
        cadena_entrada = str(input("Ingrese una cadena de numeros: "))
        while (len(cadena_entrada) != largo_cadena):
            print("La cadena es incorrecta")
            cadena_entrada = str(input("Ingrese una cadena de numeros: "))
        else: 
                
            lista_entrada = []
            for nro_input in cadena_entrada:
                lista_entrada.append(nro_input)

            for indice in range(0, largo_cadena):
                if lista[indice] == lista_entrada[indice]:
                    contadorCifrasCorrectas +=  1

            if contadorCifrasCorrectas == largo_cadena:
                print("¡¡¡ Lo has logrado !!!")
                fin = True
            else:    
                print(f"Has acertado "+ str(contadorCifrasCorrectas) + " numeros. Inténtalo de nuevo")        

aproximar_cadena(var)



