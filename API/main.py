from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def ruta1():
    return{"mensaje":"Bienvenida a tu primera api"}
