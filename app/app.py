from beanie import init_beanie
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from app.api.api_v1.router import router
from app.core.config import settings
from app.models.todo_model import Todo
from app.models.user_model import User

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def app_init():
    """
    Initialize crucial application services
    """
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).todolist
    await init_beanie(database=db_client, document_models=[User, Todo])

# Register the startup event handler
app.add_event_handler("startup", app_init)

# Include your router after initializing services
app.include_router(router, prefix=settings.API_V1_STR)
