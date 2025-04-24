from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

API_KEY = "**********************"
BASE_URL = "**********************************"


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
