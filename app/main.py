from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.db import engine, Base
from app.api.routes.todo import router as api_router

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI()

# Define allowed origins for CORS
origins = [
    "*",
    "http://127.0.0.1:5500",
    "http://localhost:5500"
] 

# Add CORS middleware to allow specific origins and methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
    
    
)

# Include the API router
app.include_router(api_router, prefix="/api/v1")
