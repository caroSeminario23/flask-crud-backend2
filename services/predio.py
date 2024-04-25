from flask import Blueprint, request, json, jsonify 
from model.predio import Predio
from utils.db import db

predios = Blueprint('predios', __name__) # Permite crear una instancia personalizada

@predios.route('/predios/v1', methods =['GET']) 
def getMensaje():
    result = {}
    result["data"]='flask-crud-backend2'
    return jsonify(result) # Permite retornar el resultado

@predios.route('/predios/v1/listar', methods =['GET']) # Se define el tipo de petición que puede atender la app
def getPredio():
    result = {}
    predios = Predio.query.all() # Equivalente a hacer un SELECT (especificaciones propias del ORM)
    result["data"]=predios
    result["status_code"]=200 # Indica el código de estado de la solicitud
    result["message"]="Se recuperó los predios sin inconvenientes"
    return jsonify(result), 200 # Permite retornar el resultado

@predios.route('/predios/v1/insert', methods =['POST']) # Se define el tipo de petición que puede atender la app
def insert():
    result = {} # Se crea un diccionario vacío
    body = request.get_json() # Se obtiene el contenido de la petición

    id_tipo_predio=body.get("id_tipo_predio")
    id_persona=body.get("id_persona")
    total_mdu=body.get("total_mdu")
    description=body.get("description")
    ruc=body.get("ruc")
    telefono=body.get("telefono")
    correo=body.get("correo")
    direccion=body.get("direccion")
    idubigeo=body.get("idubigeo")
    url_imagen=body.get("url_imagen")
    
    if not id_tipo_predio or not description or not ruc or not telefono or not correo or not direccion or not idubigeo or not id_persona or not url_imagen or not total_mdu: # Si no se obtiene alguno de los valores solicitados
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result), 400
    
    predio = Predio(id_tipo_predio, description, ruc, telefono, correo, direccion, idubigeo, id_persona, url_imagen, total_mdu) # Se crea una instancia de la clase Contact con los valores obtenidos
    db.session.add(predio) # Se agrega el contacto a la sesión
    db.session.commit() # Se confirma la transacción
    result['data']=predio # Se obtiene el id del contacto
    result['status_code']=201 # Indica el código de estado de la solicitud
    result['msg']="Faltan datos 2" # Indica el mensaje de la solicitud
    return jsonify(result), 201 # Permite retornar el resultado

@predios.route('/predios/v1/update', methods =['POST']) # Se define el tipo de petición que puede atender la app
def update():
    result = {}
    body=request.get_json()

    id_predio = body.get('id')
    id_tipo_predio = body.get('id_tipo_predio')
    description = body.get('description')
    ruc = body.get('ruc')
    telefono = body.get('telefono')
    correo = body.get('correo')
    direccion = body.get('direccion')
    idubigeo = body.get('idubigeo')
    id_persona = body.get('id_persona')
    url_imagen = body.get('url_imagen')
    total_mdu = body.get('total_mdu')

    if not id_predio or not id_tipo_predio or not description or not ruc or not telefono or not correo or not direccion or not idubigeo or not id_persona or not url_imagen or not total_mdu: # Si no se obtiene alguno de los valores solicitados
        result["status_code"]=400
        result["message"]="Faltan datos"
        return jsonify(result), 400
    
    predio = Predio.query.get(id) # Se obtiene el contacto con el id especificado en la petición
    if not predio: # Si no se encuentra el contacto
        result["status_code"]=400
        result["message"]="Predio no existe"
        return jsonify(result), 400
    
    predio.id_tipo_predio = id_tipo_predio
    predio.description = description
    predio.ruc = ruc
    predio.telefono = telefono
    predio.correo = correo
    predio.direccion = direccion
    predio.idubigeo = idubigeo
    predio.id_persona = id_persona
    predio.url_imagen = url_imagen
    predio.total_mdu = total_mdu

    db.session.commit() # Se confirma la transacción

    result['data']=predio # Se obtiene el id del contacto

@predios.route('/predios/v1/delete', methods =['DELETE']) # Se define el tipo de petición que puede atender la app
def delete():
    result = {}
    body=request.get_json() # Se obtiene el contenido de la petición
    id=body.get('id_predio') # Se obtiene el valor de la clave id (se captura) 

    if not id: # Si no se obtiene el id del contacto
        result["status_code"]=400
        result["message"]="Debe consignar un id válido"
        return jsonify(result), 400
    
    predio = Predio.query.get(id) # Se obtiene el contacto con el id especificado en la petición
    if not predio: # Si no se encuentra el contacto
        result["status_code"]=400
        result["message"]="Predio no existe"
        return jsonify(result), 400
    
    db.session.delete(predio) # Se elimina el contacto
    db.session.commit()
    result['data']=predio
    result['status_code']=200
    result['msg']="Predio eliminado"
    return jsonify(result), 200

