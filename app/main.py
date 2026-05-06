from fastapi import FastAPI
from app.routes.users import router

app = FastAPI()

# simple test route
@app.get("/health")
def health():
    return {"status": "ok"}

# include all user routes
app.include_router(router)