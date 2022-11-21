import requests
url = "http://127.0.0.1:8000"

# buscar filtrando todos los parámetro
def get_desempleo(year, month, district, barrio, gender, status_desempleo):
    return requests.get(url + f"/desempleo?year={year}&month={month}&district={district}&barrio={barrio}&gender={gender}&status={status_desempleo}").json()

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

# buscar filtrando por estado
def get_status():
    return requests.get(url + "/status/all").json()

# buscar total por año
def desempleo_anual():
    return requests.get(url + "/desempleo/total/year").json()


# buscar total por género
def desempleo_genero():
    return requests.get(url + "/desempleo/total/genero").json()

# buscar total por distrito
def desempleo_por_distrito():
    return requests.get(url + "/desempleo/total/distrito").json()