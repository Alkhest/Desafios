from fastapi import FastAPI
from pydantic import BaseModel
import json
import requests
import datetime

appIndi = FastAPI()


class DatosIndi(BaseModel):
    indi: str
    date: datetime.date

@appIndi.get("/indicadores/{indicador}/{year}")
def getIndicadores(indicador, year):

    DatosIndi.indi = indicador
    DatosIndi.date = year 
    
    # En este caso hacemos la solicitud para el caso de consulta de un indicador en un año determinado
    url = f'https://mindicador.cl/api/{DatosIndi.indi}/{DatosIndi.date}'
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    # Para que el json se vea ordenado, retornar pretty_json
    pretty_json = json.dumps(data, indent=2)
    return data

@appIndi.get("/indicadores/{indicador}/")
def getOnlyIndicadores(indicador):

    DatosIndi.indi = indicador
    # En este caso hacemos la solicitud para el caso de consulta de un indicador en un año determinado
    url = f'https://mindicador.cl/api/{DatosIndi.indi}/'
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    # Para que el json se vea ordenado, retornar pretty_json
    pretty_json = json.dumps(data, indent=2)
    return data

@appIndi.get("/indicadores/")
def getAllIndicadores():    
    
    # En este caso hacemos la solicitud para el caso de consulta de un indicador en un año determinado
    url = f'https://mindicador.cl/api/'
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    # Para que el json se vea ordenado, retornar pretty_json
    pretty_json = json.dumps(data, indent=2)
    return data