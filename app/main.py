from fastapi import FastAPI, Request
from app.routes.users import router
from app.logger import logger
from app.metrics import total_requests, error_count
import time
import app.metrics as metrics

app = FastAPI()


# middleware
@app.middleware("http")
async def track_metrics(request: Request, call_next):

    # count requests
    metrics.total_requests += 1

    # start timer
    start_time = time.time()

    try:
        response = await call_next(request)

        # compute response time
        process_time = time.time() - start_time

        logger.info(
            f"{request.method} {request.url.path} | "
            f"Status: {response.status_code} | "
            f"Response time: {process_time:.4f}s"
        )

        return response

    except Exception as e:

        # count errors
        metrics.error_count += 1

        logger.error(f"Error: {str(e)}")
        raise e


# health endpoint
@app.get("/health")
def health():
    return {"status": "ok"}


# metrics endpoint
@app.get("/metrics")
def get_metrics():
    return {
        "total_requests": metrics.total_requests,
        "error_count": metrics.error_count
    }


# routes
app.include_router(router)