from fastapi import FastAPI, Request
from pydantic import BaseModel
import datetime

app = FastAPI()

class Vector(BaseModel):
    x: float
    y: float
    z: float

class IMUData(BaseModel):
    accel: Vector
    gyro: Vector

@app.post("/imu-data")
async def receive_imu_data(data: IMUData):
    # Store to DB, file, or just print
    print(f"[{datetime.datetime.now()}] Accel: {data.accel}, Gyro: {data.gyro}")
    return {"message": "IMU data received successfully"}
 
