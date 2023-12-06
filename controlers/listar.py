from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

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

class RegistroPintura(BaseModel):
    titulo: str
    estilo: str
    tecnica: str
    precio: float

registroslogin = []

@app.post("/registrar_pintura", response_model=RegistroPintura)
def registrar_pintura(registro: RegistroPintura):
    registroslogin.append(registro)
    return registro

@app.get("/listar_registros")
def listar_registros():
    if not registroslogin:
        raise HTTPException(status_code=404, detail="No hay registros para listar")
    return registroslogin

@app.delete("/eliminar_registro/{index}")
def eliminar_registro(index: int):
    if index < 0 or index >= len(registroslogin):
        raise HTTPException(status_code=404, detail="Índice de registro no válido")
    del registroslogin[index]
    return {"message": "Registro eliminado exitosamente"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
