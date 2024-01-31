from sqlalchemy import Column, Integer, String, DateTime, ForeignKey , create_engine , Boolean ,MetaData , Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from databases import Database
from datetime import datetime

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} , echo=True)
metadata = MetaData()

Base = declarative_base() # ORM
 
todos = Table(
    
    "todos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(255)),
    Column("description", String(255)),
    Column("is_completed", Boolean, default=False),
    
)
    
database  = Database(DATABASE_URL)