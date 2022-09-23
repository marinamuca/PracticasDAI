#./app/app.py
from flask import Flask
app = Flask(__name__)

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
