import requests
url = "http://127.0.0.1:8000"

# buscar filtrando todos los parámetro
def get_desempleo(year, month, district, barrio, gender):
    return requests.get(url + f"/desempleo?year={year}&month={month}&district={district}&barrio={barrio}&gender={gender}").json()

# buscar filtrando los años diferentes de la colección
def get_years():
    return requests.get(url + "/year/all").json()

# buscar filtrando los meses diferentes de la colección
def get_month():
    return requests.get(url + "/month/all").json()

# buscar filtrando los distritos diferentes de la colección
def get_district():
    return requests.get(url + "/district/all").json()

# buscar filtrando los distintos barrios de los diferentes distritos de la colección
def get_barrio(district):
    return requests.get(url + f"/barrio/all?distrito={district}").json()

# buscar filtrando por género
def get_gender():
    return requests.get(url + "/gender/all").json()