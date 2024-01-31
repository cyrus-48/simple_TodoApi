from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.db import engine, metadata , Base
from app.api.routes.todo import router as api_router


Base.metadata.create_all(bind=engine)
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


app.include_router(api_router, prefix="/api/v1")
