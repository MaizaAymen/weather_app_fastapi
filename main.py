from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

API_KEY = "87bdf686e84f5a6de051ae507ec00cdb"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


class WeatherReq(BaseModel):
    city:str
class WeatherRes(BaseModel):
    city:str
    temperature:float
    description:str

@app.post("aymen",response_model=WeatherRes)
def get_weather(request:WeatherReq):
    parms ={
        "q":request.city,
        "appid":API_KEY,
        "units":"metric"
    }
    response=requests.get(BASE_URL,params=parms)
    data=response.json()


    if response.status_code !=200:
        raise HTTPException(status_code=response.status_code,detail=response.text)


    Weather= WeatherRes(
        city=data["city"],
        temperature=data["main"]["temp"],
        description=data["weather"][0]["description"],
    )
    return Weather
