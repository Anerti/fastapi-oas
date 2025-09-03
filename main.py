import json
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

app = FastAPI()


class Characteristics(BaseModel):
    max_speed: int
    max_fuel_capacity: int


class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristics


cars_lists: List[Car] = []


@app.get("/ping")
def hello():
    return Response(content="pong", status_code=200, media_type="text/plain")


@app.get("/cars")
def welcome(name: str):
    return Response(content=f"Welcome {name}!", status_code=200, media_type="text/plain")


@app.post("/cars")
def create_cars(car: List[Car]):
    cars_lists.extend(car)
    serialized_car = []
    for car in cars_lists:
        serialized_car.append(s.model_dump())
    return JSONResponse(content=serialized_car, status_code=201, media_type="application/json")


@app.get("/cars")
def read_cars():
    deserialized_car = []
    for car in cars_lists:
        deserialized_car.append(s.model_dump())
    return JSONResponse(content=cars_lists, status_code=200, media_type="application/json")


@app.get("/cars/{id}")
def getting_car_by_id(id_fetched: id):
    for car in cars_lists: 
        if car.id == id_fetched:
            return JSONResponse(content=car, status_code=200, media_type="application/json")
    return JSONResponse(content=f"car with {id_fetched} not found", status_code=404, media_type="text/plain")


@app.put("/cars/{id}/characteristics")
def update_car_characteristics(fetched_id: str, new_characteristics: Characteristics):
    for car in car_list:
        if car.id == fetched_id:
            car.characteristics = new_characteristics
            return Response(content=f"{fetched_id} updated successfully", status_code=200, media_type="text/plain")
    return Response(content=f"Car with {fetched_id} not found", status_code=404, media_type="text/plain")
