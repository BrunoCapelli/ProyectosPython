################################
# Ejercicio 1
# Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""
def max(num1, num2):
    if num1 > num2:
        print("El mayor numero es "+ num1)
    else:
        print("El mayor numero es " + num2)


num1 = input("Ingrese un numero: ")
num2 = input("Ingrese el segundo numero: ")

max(num1,num2)
"""
###################################
#       Ejercicio 2
# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""
def max_de_tres(num1,num2,num3):
    if (num1 - (num2+num3)) > 0:
        print("El mayor numero es "+ str(num1))
    else:
        if num2>num3:
            print("El numero mas grande es "+ str(num2))
        else:
            print("El numero mas grande es "+ str(num3))

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

max_de_tres(num1,num2,num3)
"""

#       Ejercicio 3
# Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""
fin = "fin"
entrada=""
contador = 0
while entrada != fin:
    entrada = input("Ingrese datos: ")
    contador= contador + 1
else:
    print(contador)

def longitud(cadena):
    contador= 0
    for elemento in cadena:
        contador += 1
    return print(contador)

cadena=input("Ingrese una cadena: ")

longitud(cadena)
"""

#       Ejercicio 4
#  Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False. #

"""
param = input("Ingrese una letra: ")
def vocal(param):
    result =""
    if param == "a":
        result = "True"
    else:
        if param == "e":
            result = "True"
        else:
            if param == "i":
                result= "True"
            else:
                if param == "o":
                    result= "True"
                else:
                    if param == "u":
                        result= "True"
                    else:
                        result="False"
    
    return print(result)
    

vocal(param)
"""
"""
#       Ejercicio 5
# Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.


def sum(num1,num2,num3,num4):
    suma= num1+num2+num3+num4
            
    return print(suma)

sum(6,7,8,9)

def pro(num1,num2,num3,num4):
    prod= num1*num2*num3*num4
            
    return print(prod)

pro(6,7,8,9)
"""
"""
#   Ejercicio 6
#    Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

cadena = input("Escribir algo: ")
def inve(cadena):
    cadena_invertida= ""
    for elemento in cadena:
        cadena_invertida= elemento + cadena_invertida
    return print("Al reves: "+ cadena_invertida)

inve(cadena)

"""
""""
#    Ejercicio 7
#    Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

cadena= input("¿Es palindromo?: ")
def es_palindromo(cadena):
    cadena_invertida= ""
    for elemento in cadena:
        cadena_invertida= elemento + cadena_invertida
    if cadena == cadena_invertida:
        print("True")
    else:
        print("False")

es_palindromo(cadena)

"""
"""
#      Ejercicio 8
# Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

entrada1 = input("Ingrese la primer lista: ")
entrada2 = input("Ingrese la segunda lista: ")


def superPosicion():
    for elemento in entrada1:
        for elemento1 in entrada2:
            if elemento == elemento1:
                result = (True)
            else:
                result= False
    return print(result)

superPosicion()

"""
"""
#   Ejercicio 9
# Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".


def generar_n_caracteres(num, letra):
    result=""
    for elemento in range(0,num):
        result= result + letra
    return print(result)

generar_n_caracteres(5, "m")

"""

#       Ejercicio 10
# Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

"""
def histograma(param):
    result=""
    for elemento in param:
        for cosa in range(0,elemento):
            result = result + "*"
        print(result)
        result=""

histograma([9,4,6,2,3,8,6])
"""