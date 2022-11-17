from fastapi import APIRouter
from database.mongo import db
from bson import json_util
from json import loads

router=APIRouter()

@router.get("/desempleo/{year}")
def desempleo_by_year(year:int):
    filter = {"Year":year}
    project = {"_id":0}
    res = db["Desempleo"].find(filter, project)
    return loads(json_util.dumps(res))

@router.get("/desempleo/year")
def desempleo_by_year(year:int):
    filter = {"Year":year}
    project = {"_id":0}
    res = db["Desempleo"].find(filter, project)
    return loads(json_util.dumps(res))

@router.get("/desempleo")
def desempleo_by_all(dist:str,year:int, month:str):
    res = db["Desempleo"].find({"District Name":dist, "Year":year, "Month":month}, {"_id":0})
    return loads(json_util.dumps(res))

@router.get("/desempleo")
def desempleo_by_all(dist:str, year:int, month:str, gender:str):
    res = db["Desempleo"].find({"District Name":dist, "Year":year, "Month":month, "Gender":gender})
    return loads(json_util,dumps(res))