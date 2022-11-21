from fastapi import APIRouter
from database.mongo import db
from bson import json_util
from json import loads
from calendar import month_name


router=APIRouter()

# Filtrado por año
@router.get("/desempleo/{year}")
def desempleo_by_year(year:int):
    filter = {"Year":year}
    project = {"_id":0}
    res = db["Desempleo"].find(filter, project)
    return loads(json_util.dumps(res))
 
# Filtrado por año, mes, distrito, barrio y género
@router.get("/desempleo")
def desempleo_by_all(year:int, month:str, district:str, barrio:str, gender:str, status:str):
    filter = {"Year":year, "Month":month, "District Name": district, "Neighborhood Name":barrio, "Gender":gender, "Demand_occupation":status}
    project = {"_id":0}
    res = db["Desempleo"].find(filter, project)
    return loads(json_util.dumps(res))

# Retorna los distintos años de toda la colección
@router.get("/year/all")
def years_disponibles():
    res = db["Desempleo"].distinct("Year")
    return res

# Retorna los distintos meses de toda la colección
@router.get("/month/all")
def meses_disponibles():
    res = db["Desempleo"].distinct("Month")
    month_lookup = list(month_name)
    return sorted(res, key=month_lookup.index)
 
# Retorna los distintos distritos de toda la colección
@router.get("/district/all")
def distritos_disponibles():
    res = db["Desempleo"].distinct("District Name")
    return res

# Retorna los distintos barrios de toda la colección
@router.get("/barrio/all")
def barrios_disponibles(distrito):
    filter = {"District Name":distrito}
    res = db["Desempleo"].find(filter).distinct("Neighborhood Name")
    return res

# Retorna los distintos géneros de toda la colección
@router.get("/gender/all")
def generos_disponibles():
    return ["Male", "Female"]

# Retorna el estado de desempleo
@router.get("/status/all")
def estado_desempleo():
    return ["Registered unemployed", "Unemployment demand"] 

# Endpoint que devuelve el desempleo total de cada año
@router.get("/desempleo/total/year")
def desempleo_total_year():
    res = db["Desempleo"].aggregate([{"$group": {"_id": "$Year", "desempleo_total":{"$sum":"$Number"}}}])
    return loads(json_util.dumps(res))

# Endpoint que devuelve el género
@router.get("/desempleo/total/genero")
def desempleo_total_genero():
    res = db["Desempleo"].aggregate([{"$group": {"_id": "$Gender", "desempleo_total":{"$sum":"$Number"}}}])
    return loads(json_util.dumps(res))

# Endpoint que devuelve el desempleo por distrito
@router.get("/desempleo/total/distrito")
def desempleo_total_distrito():
    res = db["Desempleo"].aggregate([{"$group": {"_id": "$District Name", "desempleo_total":{"$sum":"$Number"}}}])
    return loads(json_util.dumps(res))

