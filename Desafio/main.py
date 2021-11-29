from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json
import requests


appIndi = FastAPI()

#Parametros de entrada necesarios.
class DatosIndi(BaseModel):
    #Listado de indicadores comerciales    
    indicadores: List[str] = []
    #Año de consulta
    date: str
    
#Metodo encargado de obtener 3 o más indicadores por año solicitado.
@appIndi.post("/indicadores")
def getMinIndicadores(datos: DatosIndi):    
    #Lista para almacenar datos de salida
    result = []

    #Validar que los indicadores comerciales sean minimo 3
    if len(datos.indicadores) < 3:
        return "Debe ingresar 3 o más indicacores."

    #Se recorre listado de indicadores solicitados
    for indi in datos.indicadores:
        # Se llama al servicio.
        url = f'https://mindicador.cl/api/{indi}/{datos.date}'
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        #Se lista lo obtenido
        result.append(data)
    #Se retorna listado de lo solicitado      
    return result
