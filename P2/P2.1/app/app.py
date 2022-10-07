#./app/app.py
from dataclasses import replace
from urllib import response
from xmlrpc.client import ResponseError
from bson.json_util import dumps
from pymongo import MongoClient

from flask import Flask, Response

app = Flask(__name__)

# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)

# Base de datos
db = client.cockteles

@app.route('/todas_las_recetas')
def mongo():
    # Encontramos los documentos de la coleccion "recipes"
    recetas = db.recipes.find() # devuelve un cursor(*), no una lista ni un iterador

    lista_recetas = []
    for  receta in recetas:
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')

@app.route('/receta_de/<slug>')
def receta_de(slug):
    regexpr = "(?i)" + slug.replace("_", "-")
    response = db.recipes.find({"slug":  {"$regex": regexpr } })
    resJson = dumps(response)
    return Response(resJson, mimetype='application/json')

@app.route('/receta_con/<ingr>')
def receta_con(ingr):
    regexpr = "(?i)" + ingr.replace("_", " ")
    response = db.recipes.find({ "ingredients": { "$elemMatch": {"name": {"$regex": regexpr }} } })
    resJson = dumps(response)
    return Response(resJson, mimetype='application/json')

@app.route('/receta_compuesta_de/<int:number>/<nombre_array>')
def receta_compuesta_de(number, nombre_array):
    response = db.recipes.find( { nombre_array: { "$size": number } } )
    resJson = dumps(response)
    return Response(resJson, mimetype='application/json')

# @app.route('/ingredientes de/<receta>')
# def ingredientes_de(receta):
#     receta_de(receta)
#     resJson = dumps(response)
#     return Response(resJson, mimetype='application/json')

