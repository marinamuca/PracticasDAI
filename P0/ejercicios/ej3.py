# Generar secuencia aleatoria de [ y ]

import random

def generarCadena():
    corchetes = ["[", "]"]
    return ''.join(random.choice(corchetes) for x in range(random.randrange(11)))

# Comprobar si está balanceada
cadena = generarCadena()
# cadena = "[]][][]["

print("Cadena generada: ", cadena)
balance = 0

firstOpen = True
for c in cadena:
    if c == "[":
       balance+=1
    else :
        if balance == 0:
            firstOpen = False
            break
        else:
            balance -=1

if (firstOpen):
    if (balance > 0):
        print("La cadena no está balanceada")
    else:
        print("La cadena está balanceada")
else:
    print("La cadena no está balanceada")
