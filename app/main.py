from fastapi import FastAPI, Request
from app.routes.users import router
from app.logger import logger
import time
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()


# ✅ Prometheus automatic metrics
Instrumentator().instrument(app).expose(app)


# =========================
# Middleware (logging only)
# =========================
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    try:
        response = await call_next(request)

        process_time = time.time() - start_time

        logger.info(
            f"{request.method} {request.url.path} | "
            f"Status: {response.status_code} | "
            f"Time: {process_time:.4f}s"
        )

        return response

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise e


# =========================
# Health check
# =========================
@app.get("/health")
def health():
    return {"status": "ok"}


# =========================
# Routes
# =========================
app.include_router(router)