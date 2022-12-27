#./app/app.py
from dataclasses import replace
import json
from urllib import response
from xmlrpc.client import ResponseError
from bson.json_util import dumps
from pymongo import MongoClient
from bson import ObjectId
from flask import Flask, Response, request, jsonify, render_template
from flask_restful import Resource, Api

app = Flask(__name__)

# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)

# Base de datos
db = client.cockteles

# PRACTICA 2 - PARTE 1

def buscar(id):
    buscado = db.recipes.find_one({'_id':ObjectId(id)})
    if buscado:
            buscado['_id'] = str(buscado['_id']) # casting a string (es un ObjectId)
            return jsonify(buscado)
    else:
        return jsonify({'error':'Not found'}), 404


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


# PRACTICA 2 - PARTE 2

# para devolver una lista (GET), o añadir (POST)
@app.route('/api/recipes', methods=['GET', 'POST'])
def api_1():
    if request.method == 'GET':
        lista = []
        buscados = db.recipes.find().sort('name')
        for recipe in buscados:
            recipe['_id'] = str(recipe['_id']) # casting a string (es un ObjectId)
            lista.append(recipe)
        return jsonify(lista)

    if request.method == 'POST':
        creado = db.recipes.insert_one(json.loads(request.data))
        return dumps(db.recipes.find_one({'_id':creado.inserted_id}))
         
           
# para devolver una, modificar o borrar
@app.route('/api/recipes/<id>', methods=['GET', 'PUT', 'DELETE'])
def api_2(id):
    if request.method == 'GET':
        ingredient = request.args.get("con")
        if ingredient:
            regexpr = "(?i)" + ingredient.replace("_", " ")
            response = db.recipes.find({ "ingredients": { "$elemMatch": {"name": {"$regex": regexpr }} } })
            resJson = dumps(response)
            return Response(resJson, mimetype='application/json')
        else:
            return buscar(id)
    if request.method == 'PUT':
        db.recipes.update_one({'_id': ObjectId(id)}, {"$set": json.loads(request.data)})
        return buscar(id)

    if request.method == 'DELETE':
        eliminado = buscar(id)
        db.recipes.delete_one({'_id': ObjectId(id)})
        return eliminado
     
# PRACTICA 2 - PARTE 2 usando flask restful

api = Api(app)

class Recipes(Resource):
    def get(self):
        ingredient = request.args.get("con")
        if ingredient:
            regexpr = "(?i)" + ingredient.replace("_", " ")
            response = db.recipes.find({ "ingredients": { "$elemMatch": {"name": {"$regex": regexpr }} } })
            resJson = dumps(response)
            return Response(resJson, mimetype='application/json')
        else:
            lista = []
            buscados = db.recipes.find().sort('name')
            for recipe in buscados:
                recipe['_id'] = str(recipe['_id']) # casting a string (es un ObjectId)
                lista.append(recipe)
            return jsonify(lista)
    def post(self):
        creado = db.recipes.insert_one(json.loads(request.data))
        resJson = dumps(db.recipes.find_one({'_id':creado.inserted_id}))
        return Response(resJson, mimetype='application/json')

class RecipesID(Resource):
    def get(self, id):
        return buscar(id)

    def put(self, id):
        db.recipes.update_one({'_id': ObjectId(id)}, {"$set": json.loads(request.data)})
        return buscar(id)

    def delete(self, id):
        eliminado = buscar(id)
        db.recipes.delete_one({'_id': ObjectId(id)})
        return eliminado

@app.route('/')
def index():
    return render_template('index.html')

api.add_resource(Recipes, '/api/v2/recipes')
api.add_resource(RecipesID, '/api/v2/recipes/<id>')