from sqlalchemy import Column, Integer, String, DateTime, ForeignKey ,Text, create_engine , Boolean ,MetaData , Table
from sqlalchemy.orm import relationship , sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from databases import Database 

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} , echo=True)
metadata = MetaData()

SessionLocal  = sessionmaker(autocommit=False, autoflush=False, bind=engine)

 
Base  = declarative_base()
meatadat = MetaData()

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    title  = Column(String(100), nullable=False)
    description = Column(String(), default="")
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    
def get_db():
    try:
        db = SessionLocal()
        yield db
        
    finally:
        db.close()



    