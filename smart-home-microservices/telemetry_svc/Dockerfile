FROM python:3.11.9-slim as python-stage
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_ROOT_USER_ACTION=ignore
ENV PYTHONPYCACHEPREFIX=/app/

FROM python-stage as requirements-stage
WORKDIR /app/
COPY telemetry_svc/requirements.txt /app/requirements.txt

FROM python-stage as base-stage
WORKDIR /code/telemetry_svc/
ENV PYTHONPATH=$PYTHONPATH:/code/telemetry_svc/src/
COPY --from=requirements-stage /app/requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY telemetry_svc/src /code/telemetry_svc/src

FROM base-stage as api-stage