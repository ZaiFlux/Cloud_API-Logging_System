from fastapi import FastAPI, Request
from app.routes.users import router
from app.logger import logger

app = FastAPI()

# logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):

    logger.info(f"Request: {request.method} {request.url.path}")

    try:
        response = await call_next(request)

        logger.info(
            f"Response: {response.status_code} | {request.method} {request.url.path}"
        )

        return response

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise e


# simple test route
@app.get("/health")
def health():
    return {"status": "ok"}


# include all user routes
app.include_router(router)