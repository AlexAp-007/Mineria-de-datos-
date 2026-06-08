nombres = ["Juan", "Ana", "Juan", "Pedro", "Ana", "Juan"]

contador = {}

for nombre in nombres:
    if nombre in contador:
        contador[nombre] += 1
    else:
        contador[nombre] = 1

print(contador)