## Как запустить проект
Для старта проекта необходимо выполнить запуск `docker-compose`:
```shell
docker compose up --build
```

### Конфигурация Kafka
После запуска контейнеров следует настроить топики в Kafka. Для этого выполните следующие команды:

1. Создание топика `device_commands`:
```shell
docker compose exec -T kafka kafka-topics --create \
  --topic device_commands \
  --partitions 3 \
  --replication-factor 1 \
  --if-not-exists \
  --bootstrap-server kafka:29092
```

2. Создание топика `device_statuses`:
```shell
docker compose exec -T kafka kafka-topics --create \
  --topic device_statuses \
  --partitions 3 \
  --replication-factor 1 \
  --if-not-exists \
  --bootstrap-server kafka:29092
```

3. Создание топика `sensor_data`:
```shell
docker compose exec -T kafka kafka-topics --create \
  --topic sensor_data \
  --partitions 3 \
  --replication-factor 1 \
  --if-not-exists \
  --bootstrap-server kafka:29092
```

### Конфигурация Kong
Настройте маршруты и сервисы Kong для взаимодействия с API-сервисами:

1. Создание сервиса `device-api`:
```shell
curl -i -X POST http://localhost:8001/services/ \
  --data "name=device-api" \
  --data "url=http://device-api:8000"
```

2. Добавление маршрута для `device-api`:
```shell
curl -i -X POST http://localhost:8001/services/device-api/routes \
  --data "paths[]=/device-service"
```

3. Создание сервиса `telemetry-api`:
```shell
curl -i -X POST http://localhost:8001/services/ \
  --data "name=telemetry-api" \
  --data "url=http://telemetry-api:8000"
```

4. Добавление маршрута для `telemetry-api`:
```shell
curl -i -X POST http://localhost:8001/services/telemetry-api/routes \
  --data "paths[]=/telemetry-service"
```

### Доступ к сервисам
После выполнения вышеуказанных настроек, сервисы становятся доступны по следующим адресам:
- **Device API через Kong**: [http://localhost:8000/device-service](http://localhost:8000/device-service)
- **Telemetry API через Kong**: [http://localhost:8000/telemetry-service](http://localhost:8000/telemetry-service)
- **Kong Admin API**: [http://localhost:8001/](http://localhost:8001/)

---

## Тестирование
### Работа с `device-service`

1. Получение информации об устройстве:
```shell
curl --location 'http://0.0.0.0:8000/device-service/devices/1'
```

2. Обновление статуса устройства:
```shell
curl --location --request PUT 'http://0.0.0.0:8000/device-service/devices/1/status' \
  --header 'Content-Type: application/json' \
  --data '{
    "status": false
  }'
```

3. Отправка команды устройству:
```shell
curl --location 'http://0.0.0.0:8000/device-service/devices/1/commands' \
  --header 'Content-Type: application/json' \
  --data '{
    "command": "test command name",
    "parameters": {
        "foo": "bar",
        "test_arg": "test_var"
    }
  }'
```

### Работа с `telemetry-service`

1. Получение последней телеметрии устройства:
```shell
curl --location 'http://0.0.0.0:8000/telemetry-service/devices/1/telemetry/latest'
```

2. Получение всей телеметрии устройства:
```shell
curl --location 'http://0.0.0.0:8000/telemetry-service/devices/1/telemetry'
```