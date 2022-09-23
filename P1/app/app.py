#./app/app.py
from math import sqrt
import random
from flask import Flask
app = Flask(__name__)

def generarCadena():
    corchetes = ["[", "]"]
    return ''.join(random.choice(corchetes) for x in range(random.randrange(11)))

def corchetes(cadena):
  # Comprobar si está balanceada
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
  balanceada = False
  if (firstOpen and balance == 0):
      balanceada = True
  return balanceada
  # else:
  #     return "La cadena "+ cadena +" no está balanceada"

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/fibonacci/<int:number>')
def fibonacci(number):
  sucesion = [0,1]

  for i in range (2, number):
    suma = sucesion[i-2] + sucesion[i-1]
    sucesion.append(suma)
  return 'El término numero ' + str(number) + ' de la sucesión de fibonacci es: ' + str(sucesion[number-1])


@app.route('/eratostenes/<int:n>')
def eratostenes(n):
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

  result = ''
  for i in range (2, n+1):
      if not marcados[i-2]:
          result += str(naturales[i-2]) + ' '

  return result

@app.route('/corchetes')
def cochetes_random():
  cadena = generarCadena()
  balanceada = corchetes(cadena)
  if balanceada:
    return "La cadena "+ cadena +" está balanceada"
  else:
    return "La cadena "+ cadena +" no está balanceada"


@app.route('/corchetes/<cadena>')
def cochetes_input(cadena):
  balanceada = corchetes(cadena)
  if balanceada:
    return "La cadena "+ cadena +" está balanceada"
  else:
    return "La cadena "+ cadena +" no está balanceada"
