from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class DeviceStatus(BaseModel):
    """Модель статуса устройства"""
    status: bool


class DeviceCommand(BaseModel):
    """Модель команды для устройства"""
    command: str
    parameters: dict


@app.get("/devices/{device_id}/telemetry/latest", response_model=dict)
async def get_latest_telemetry(device_id: int):
    """
    Получить последнюю информацию о состоянии устройства

    Args:
        device_id (int): ID устройства

    Returns:
        dict: Последняя информация о состоянии устройства
    """
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "type": "integer",
        "value": 0
    }


@app.get("/devices/{device_id}/telemetry", response_model=list[dict])
async def get_telemetry(device_id: int):
    """
    Получить информацию о состоянии устройства

    Args:
        device_id (int): ID устройства

    Returns:
        list[dict]: Информация о состоянии устройства
    """
    return [
        {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "type": "integer",
            "value": 0
        }
    ]