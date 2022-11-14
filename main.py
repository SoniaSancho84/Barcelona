from fastapi import FastAPI

app = FastAPI()

@app.get('/ruta1')
def ruta1():
    return("mensaje":"Bienvenida a tu primera api ")
