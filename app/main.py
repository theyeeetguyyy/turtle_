from fastapi import FastAPI

from app.routes.agent_routes import router as agent_router
from app.utils.logger import configure_logging


configure_logging()

app = FastAPI(title="CRM Agent System", version="0.1.0")
app.include_router(agent_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "CRM Agent System Running"}

