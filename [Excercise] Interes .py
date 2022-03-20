"""
Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en C * (1 + x/100)elevado a n (años).Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.
"""


capital = int(input("Ingrese el valor del capital en dolares: "))
interes = float(input("Ingrese el porcentaje de interés: "))
years = int((input("Ingrese la cantidad de años: ")))
resultado = (capital * (1+interes/100)** 20)

print(f"Luego de " + str(years) +" años su capital inicial se convertirá en " + "%.3f" % resultado)
#print("%.3f" % resultado)