from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Device Control API",
    description="API для управления устройствами",
    version="1.0.0"
)


class DeviceStatus(BaseModel):
    """Модель статуса устройства"""
    status: bool


class DeviceCommand(BaseModel):
    """Модель команды для устройства"""
    command: str
    parameters: dict


@app.get("/devices/{device_id}", response_model=dict)
async def get_device(device_id: int):
    """
    Получить информацию о устройстве

    Args:
        device_id (int): ID устройства

    Returns:
        dict: Информация о устройстве
    """
    return {"device_id": device_id}


@app.put("/devices/{device_id}/status", response_model=dict)
async def set_device_status(device_id: int, status: DeviceStatus):
    """
    Установить статус устройства

    Args:
        device_id (int): ID устройства
        status (DeviceStatus): Статус устройства

    Returns:
        dict: Информация о устройстве с новым статусом
    """
    if not 0 <= device_id <= 100:  # Допустимый диапазон ID устройств
        raise HTTPException(status_code=400, detail="Недопустимый ID устройства")
    return {"device_id": device_id, "status": status.status}


@app.post("/devices/{device_id}/commands", response_model=dict)
async def set_device_command(device_id: int, command: DeviceCommand):
    """
    Отправить команду устройству

    Args:
        device_id (int): ID устройства
        command (DeviceCommand): Команда для устройства

    Returns:
        dict: Информация о устройстве с командой
    """
    if not 0 <= device_id <= 100:  # Допустимый диапазон ID устройств
        raise HTTPException(status_code=400, detail="Недопустимый ID устройства")
    return {"device_id": device_id, "command": command.command, "parameters": command.parameters}