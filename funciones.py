import math

def saludo():
    print("¡Hola amigo!")

def saludo_nombre(nombre):
    print(f"¡Hola {nombre}!")

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def total_factura(cantidad, iva=21):
    return cantidad + (cantidad * iva / 100)

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura