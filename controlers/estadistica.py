from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS para permitir solicitudes desde el frontend
origins = ["http://localhost:3000"]  # Reemplaza esto con la URL de tu frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/estadistica/{opcion}")
def obtener_estadistica(opcion: int):
    registroslogin = obtener_registros()
    resultado = mi_estadistica(registroslogin, opcion)
    return {"resultado": resultado}

def obtener_registros():
    datos = localStorage.getItem("registroslogin")  # Necesitas una forma de obtener datos desde el frontend
    if datos:
        return json.loads(datos)
    else:
        return []

def mi_estadistica(registroslogin, opcion):
    i = 0
    resultado = 0
    mi_objeto = None

    if opcion == 1:
        resultado = len(registroslogin)
    elif opcion == 2:
        for i in range(len(registroslogin)):
            mi_objeto = registroslogin[i]
            resultado += int(mi_objeto["precio"])
    elif opcion == 3:
        for i in range(len(registroslogin)):
            mi_objeto = registroslogin[i]
            resultado += int(mi_objeto["precio"])
        resultado = round(resultado / len(registroslogin), 2)

    return resultado

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
