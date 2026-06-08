from funciones import *

saludo()

nombre = input("Ingresa tu nombre: ")
saludo_nombre(nombre)

numero = int(input("Ingresa un número entero positivo: "))
print("Factorial:", factorial(numero))

cantidad = float(input("Ingresa el importe sin IVA: "))
print("Total con IVA:", total_factura(cantidad))

radio = float(input("Ingresa el radio del círculo: "))
print("Área del círculo:", area_circulo(radio))

altura = float(input("Ingresa la altura del cilindro: "))
print("Volumen del cilindro:", volumen_cilindro(radio, altura))