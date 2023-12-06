from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

class Usuario(BaseModel):
    usuario: str
    contrasena: str

# Variable para simular el estado de inicio de sesión
sesion_iniciada = False

@app.post("/iniciar_sesion")
def iniciar_sesion(usuario: Usuario):
    global sesion_iniciada

    if usuario.usuario == "Admin" and usuario.contrasena == "123":
        sesion_iniciada = True
        return {"mensaje": "Inicio de sesión exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Error de usuario y/o contraseña")

@app.get("/comprobar_sesion")
def comprobar_sesion():
    return {"sesion_iniciada": sesion_iniciada}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
