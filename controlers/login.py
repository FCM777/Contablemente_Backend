# desplejar las rutas para cada componentes 
# Unificando routas con controladores
from fastapi import APIRouter
# Importando servicios
from services.usuario import listar_usuarios, obtener_usuario_x_id
from common.res import responder_json

rutas = APIRouter()

url = "/usuario"

#Create Read Update Delete

@rutas.get(url,
           response_model=[])
def lista_usuarios():
    resultado = listar_usuarios()
    return responder_json(200, "OK", resultado)

@rutas.get(url + "/{id}")
def obtiene_usuario(id:str):
    usuario = obtener_usuario_x_id(int(id))
    print(usuario)
    return responder_json(200, "ok",usuario)

@rutas.post(url)
def registra_usuario(elemento:object):
    return {}

@rutas.put(url + "/{id}")
def actualiza_usuario(id:int, elemento:object):
    return {}

@rutas.delete(url + "/{id}")
def elimina_usuario(id:int):
    return {}