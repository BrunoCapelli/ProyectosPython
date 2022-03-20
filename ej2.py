"""
#   Ejercicio 1
# Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.

def max_in_list(param):
    var = 0
    for elemento in param:
        if elemento > var:
            var = elemento
    return print(var)

max_in_list([86,34,14])

"""
"""
# Ejercicio 2
# Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

def mas_larga(param):
    var = 0  
    for elemento in param:
        largo = len(elemento)
        if largo > var:
            var = largo
    return print(var)
    

mas_larga(["bruno", "ignacio","capelli", "weisbach"])

"""
"""
# Ejercicio 3
# Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

def filtrar_palabras(param, n):
    n= int(n)
    for elemento in param:
        largo = len(elemento)
        if largo >= n:
            print(elemento)

filtrar_palabras(["cacho", "momo","juan"], 4)
"""
"""
#       Ejercicio 4
# Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

#var = "Cacho"
#print(var[0:1].isupper())

def esMayuscula(cadena):
    contador = 0
    for elemento in cadena:
        var = elemento[0:1].isupper()
        if var == True:
            contador += 1
    return print(contador)

print("Este es un contador de letras mayusculas")
cadena = input("Introduce una cadena: ")
esMayuscula(cadena)

"""
"""
#   Ejercicio 5
# Construir un pequeño programa que convierta números binarios en enteros.


def cantBinarios(binario):
    contador = 0
    for elemento in binario:
        contador+= 1
    return contador

def binAdecim(param):
    contador = cantBinarios(param)
    result = 0
    for elemento in param:
        result += (int(elemento))*(2^(contador))
        print(contador)
        contador += -1
        
    return print(result)

binAdecim("1000")
"""

#       Ejercicio 5
"""
 Construir un pequeño programa que convierta números binarios en enteros.

entrada = input("Escribe un numero binario: ")
contador = 0
for elemento in entrada:
    contador += 1

var = 1
result= 0
for cosa in entrada:
    while contador != 0:
        var = 2 * var
        contador -= 1
        result = int(cosa)*var + result


print(result)
"""


# Ejercicio 6
"""
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.



year_acutal = int(input("Ingrese el año actual: "))

nombre1 = input("Ingrese un nombre: ")
edad1 = int(input("Ingrese su fecha de nacimiento: "))
nombre2 = input("Ingrese el segundo nombre: ")
edad2 = int(input("Ingrese su fecha de nacimiento: "))
nombre3 = input("Ingrese el tercer nombre: ")
edad3 = int(input("Ingrese su fecha de nacimiento: "))

result1 = year_acutal - edad1
result2 = year_acutal - edad2
result3 = year_acutal - edad3

print(nombre1 + " cumplirá " + str(result1) )
print(nombre2 + " cumplirá " + str(result2) )
print(nombre3 + " cumplirá " + str(result3) )

"""
#       Ejercicio 7
"""
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.


tupla= []
entrada = 0
print("Ingrese las edades, al finalizar escriba end ")
while entrada != "end":
    entrada= input("Ingrese su edad: ")
    if entrada == "end":
        exit
    else:
        tupla.append(int(entrada))

for var in tupla:
       if var >20:
            print(var)
"""

#   Ejercicio 8
"""
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.


nombres = ["Cacho", "Sergio", "Ana", "Camila", "Juan", "Lourdes", "Agustina", "Micaela", "Mauricio"]
contador = 0
entrada = input("Ingrese una letra para saber la cantidad de personas: ")
for elemento in nombres:
    var = elemento[0]
    if var == entrada:
        contador += 1
print(contador)
"""

#   Ejercicio 9

"""
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.


def contar_vocales(param):
    contadorA = 0
    contadorE = 0
    contadorI = 0
    contadorO = 0
    contadorU = 0
    for elemento in param:
        for letra in elemento:
             if letra == "a" :
                contadorA += 1
             if letra == "e":
               contadorE += 1
             if letra == "i" :
                 contadorI += 1
             if letra == "o" :
                contadorO += 1
             if letra == "u":
                contadorU += 1
        for letra in elemento:
             if letra == "A" :
                contadorA += 1
             if letra == "E":
               contadorE += 1
             if letra == "I" :
                 contadorI += 1
             if letra == "O" :
                contadorO += 1
             if letra == "U":
                contadorU += 1
    print(contadorA, contadorE, contadorI, contadorO, contadorU)
    
entrada = input("Ingrese una palabra: ")
contar_vocales(entrada)
"""

#   Ejercicio 10
"""
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400


def es_bisiesto(year):
    if (year%4 == 0) and ((year%100!=0) or (year%400==0)):
        print(str(year) + " es un año bisiesto")
    else:
        print("No es un año bisiesto")

es_bisiesto(2020)
"""