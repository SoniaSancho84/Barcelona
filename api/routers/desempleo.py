from fastapi import APIrouter
from database.mongo import db
from bson import json_util
from json import loads

router=APIrouter()

@router.get("/desempleo/{year}")
def desempleo_by_year(year:int):
    filter = {"Year":year}
    project = {}
    res = db["desempleo"].find(filter, project)
    return loads(json_util.dumpls(res))

