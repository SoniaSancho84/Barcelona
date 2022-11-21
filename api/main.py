from fastapi import FastAPI
from routers import desempleo

app = FastAPI()
app.include_router(desempleo.router) 

@app.get('/')
def ruta1():
    return{"mensaje":"DESEMPLEO EN BARCELONA"}