FROM python:3.11.9-slim as python-stage
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_ROOT_USER_ACTION=ignore \
    PYTHONPYCACHEPREFIX=/app/

FROM python-stage as requirements-stage
WORKDIR /app/
COPY device_svc/requirements.txt /app/

FROM python-stage as base-stage
WORKDIR /code/device_svc/
ENV PYTHONPATH=$PYTHONPATH:/code/device_svc/src/
COPY --from=requirements-stage /app/requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY device_svc/src ./src/

FROM base-stage as api-stage