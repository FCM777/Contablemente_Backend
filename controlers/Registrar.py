from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse

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
    global registroslogin

    # Verificar si el título ya existe
    if any(r.titulo.lower() == registro.titulo.lower() for r in registroslogin):
        raise HTTPException(status_code=400, detail="El título ya existe")

    registroslogin.append(registro)
    return registro

@app.get("/listar_registros")
def listar_registros():
    return registroslogin

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
