import json
import logging
import os
import time
from typing import Callable

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from prometheus_client import Counter, Histogram, make_asgi_app


APP_NAME = "production-ready-aws-platform"
APP_ENV = os.getenv("APP_ENV", "dev")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
PORT = int(os.getenv("PORT", "8080"))


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "time": self.formatTime(record, self.datefmt),
        }
        return json.dumps(log_record)


logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())

logger.handlers.clear()
logger.addHandler(handler)


REQUEST_COUNT = Counter(
    "app_http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status_code"],
)

REQUEST_LATENCY = Histogram(
    "app_http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "endpoint"],
)


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    docs_url="/docs",
    redoc_url=None,
)


@app.middleware("http")
async def metrics_middleware(request: Request, call_next: Callable):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    endpoint = request.url.path
    method = request.method
    status_code = str(response.status_code)

    REQUEST_COUNT.labels(
        method=method,
        endpoint=endpoint,
        status_code=status_code,
    ).inc()

    REQUEST_LATENCY.labels(
        method=method,
        endpoint=endpoint,
    ).observe(duration)

    logger.info(
        f"{method} {endpoint} {status_code} duration_seconds={duration:.4f}"
    )
    return response


@app.get("/")
async def root():
    return {
        "service": APP_NAME,
        "environment": APP_ENV,
        "version": APP_VERSION,
        "status": "running",
    }


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.get("/readyz")
async def readyz():
    return {"status": "ready"}


metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)
