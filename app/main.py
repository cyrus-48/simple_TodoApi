from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.db import database, engine, metadata
from app.api.routes.todo import router as api_router


metadata.create_all(engine)
app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

app.on_event("startup")(database.connect)
app.on_event("shutdown")(database.disconnect)

app.include_router(api_router, prefix="/api/v1")
