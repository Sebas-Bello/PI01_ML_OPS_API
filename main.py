from fastapi import FastAPI
import uvicorn
from Funciones.my_functions import genero, juegos, specs, earlyacces, sentiment, metascore
from Funciones.my_model_ML import predict_price_and_rmse

app = FastAPI()

#http://127.0.0.1:8000

# Se ingresa un año y devuelve una lista con los 5 géneros con mas lanzamientos en el orden correspondiente.
@app.get("/genero/año/{año}")
async def obtener_genero_por_año(Año: str):
    return genero(Año)


# Se ingresa un año y devuelve una lista con los juegos lanzados en el año.
@app.get("/juegos/año/{año}")
async def obtener_juegos_por_año(Año: str):
    return juegos(Año)


# Se ingresa un año y devuelve una lista con los 5 specs que más se repiten en el mismo en el orden correspondiente.
@app.get("/specs/año/{año}")
async def obtener_specs_por_año(Año: str):
    return specs(Año)


# Se ingresa un año y devuelve una lista la cantidad de juegos lanzados con early access.
@app.get("/earlyacces/año/{año}")
async def obtener_earlyacces_por_año(Año: str):
    return earlyacces(Año)


# Según el año de lanzamiento, se devuelve una lista con la cantidad de registros que se encuentren categorizados con un análisis de sentimiento.
@app.get("/sentiment/año/{año}")
async def obtener_sentiment_por_año(Año: str):
    return sentiment(Año)


# Top 5 juegos según año con mayor metascore.
@app.get("/metascore/año/{año}")
async def obtener_metascore_por_año(Año: str):
    return metascore(Año)


# Ingresando estos parámetros (genero y/o earlyacces), deberíamos recibir el precio y RMC.
@app.get("/precio-rmse/genero/{genero}/accesoanticipado/{earlyaccess}")
async def obtener_precio_rmse(genero: str, earlyaccess: bool):
    return predict_price_and_rmse(genero, earlyaccess)