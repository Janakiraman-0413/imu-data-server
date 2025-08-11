from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from datetime import datetime

app = FastAPI()

# Store latest IMU data globally
latest_imu_data = {}

# Define the data structure expected from ESP32
class SensorData(BaseModel):
    ax: float
    ay: float
    az: float
    gx: float
    gy: float
    gz: float

class IMUPayload(BaseModel):
    imu1: SensorData
    imu2: SensorData

@app.post("/imu-data")
async def receive_imu_data(payload: IMUPayload):
    global latest_imu_data
    latest_imu_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "imu1": payload.imu1.dict(),
        "imu2": payload.imu2.dict()
    }
    print(f"[{latest_imu_data['timestamp']}] Data received!")
    return {"status": "success", "message": "Data stored"}

@app.get("/get-imu-data")
async def send_imu_data():
    if not latest_imu_data:
        return {"status": "no data yet"}
    return latest_imu_data



###-----------------------------------------Old - 05.08.2025----------------------------------------------###
# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# import datetime

# app = FastAPI()

# class Vector(BaseModel):
#     x: float
#     y: float
#     z: float

# class IMUData(BaseModel):
#     accel: Vector
#     gyro: Vector

# @app.post("/imu-data")
# async def receive_imu_data(data: IMUData):
#     # Store to DB, file, or just print
#     print(f"[{datetime.datetime.now()}] Accel: {data.accel}, Gyro: {data.gyro}")
#     return {"message": "IMU data received successfully"}
 
