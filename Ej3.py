
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
import random
largo_cadena = int(input("Ingrese el largo de la cadena: "))

def nro_aleatorio():
    global var
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
print(nro_random)           # Numero aleatorio
lista = []

def aproximar_cadena(var):
    contadorCifrasCorrectas = 0
    fin = False
    for num in nro_random:
            lista.append(num)
    print(lista)
    while fin == False:
        contadorCifrasCorrectas = 0
        cadena_entrada = str(input("Ingrese una cadena de numeros: "))
    
        for num in nro_random:
            for num1 in cadena_entrada:
                if num1 == num:
                    contadorCifrasCorrectas += 1
        print(f"Has acertado: "+ str(contadorCifrasCorrectas))
        print(f"Intentalo de nuevo")
        if contadorCifrasCorrectas == largo_cadena:
            print("¡Lo lograste!")
            fin = True


 
aproximar_cadena(var)



