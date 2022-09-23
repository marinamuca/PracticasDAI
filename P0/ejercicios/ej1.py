# Criba de Eratóstenes
from math import sqrt, trunc


n = int(input("Introduzca un número natural: "))
print("Se ha introducido:", n)

naturales = []
marcados = []

# inicialización de los arrays
for i in range(2, n+1):
    naturales.append(i)
    marcados.append(False)

for i in range(2, int(sqrt(n))+1) :
    if not marcados[i-2] :
        for j in range(i, n//i+1):
            marcados[i*j-2] = True

for i in range (2, n+1):
    if not marcados[i-2]:
        print(naturales[i-2])
