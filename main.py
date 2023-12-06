from fastapi import FastAPI
from registrar import RegistrarHandler
from listar import ListarHandler
from estadistica import EstadisticaHandler
from login import LoginHandler
from menu import MenuHandler

app = FastAPI()

# Crear instancias de las clases handler
registrar_handler = RegistrarHandler([])
listar_handler = ListarHandler([])
estadistica_handler = EstadisticaHandler([])
login_handler = LoginHandler([])
menu_handler = MenuHandler([])

# Rutas específicas para cada componente
@app.post("/registrar_pintura")
def registrar_pintura(registro: dict):
    return registrar_handler.registrar_pintura(registro)

@app.get("/listar_registros")
def listar_registros():
    return listar_handler.listar_registros()

# Agrega más rutas según sea necesario para los otros componentes (Estadistica, Login, Menu)
# ...

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
