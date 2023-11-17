from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"Estado": "Funcionando"}

""" @app.post("/")

@app.put("/")

@app.patch("/")

@app.delete("/") """
