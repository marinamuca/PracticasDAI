# Sucesión de Fibonacci

with open("./ej2-in.txt") as file:
    txt = file.read().split()
    number = int(txt[0])

print("Calculando la sucesión de fibonacci hasta el elemento numero", number, "... ")

sucesion = [0,1]

for i in range (2, number):
   suma = sucesion[i-2] + sucesion[i-1]
   sucesion.append(suma)

with open("./ej2-out.txt", "w") as file: #si no existe el archivo, lo crea
    file.write(str(sucesion[number-1]))