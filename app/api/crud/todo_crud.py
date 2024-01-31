from app.api.models.todo import TodoCreate, TodoUpdate , TodoInDB
from app.db import Todo, get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List , Annotated
from datetime import datetime as dt


class TodoCrud:  
    
    def __init__(self , db_session :Session = Depends(get_db)): 
        self.model  = Todo
        self.db_session  =  db_session

    async def post(self , payload: TodoCreate):  
            todo = self.model(title=payload.title, description=payload.description)
            todo.created_at = todo.updated_at = dt.now()
            self.db_session.add(todo)
            self.db_session.commit()
            self.db_session.refresh(todo)
            
            return todo 
    
    async def get_all_todos(self): 
        return self.db_session.query(self.model).all()
    async def get_one_todo_by_id(self , id: int):
        return self.db_session.query(self.model).filter(self.model.id == id).first()
    async def put(self , id: int , payload: TodoUpdate): 
        todo = self.db_session.query(self.model).filter(self.model.id == id).first()
        todo.title = payload.title
        todo.description = payload.description
        todo.updated_at = dt.now()
        self.db_session.commit()
        self.db_session.refresh(todo)
        return todo
    
    async def delete(self , id: int): 
        todo = self.db_session.query(self.model).filter(self.model.id == id).first()
        self.db_session.delete(todo)
        self.db_session.commit()
        return todo
    
    async def get_all_todos_completed(self): 
        return self.db_session.query(self.model).filter(self.model.is_completed == True).all()
    async def get_all_todos_not_completed(self): 
        return self.db_session.query(self.model).filter(self.model.is_completed == False).all()
    async def put_completed(self , id: int):  
        todo = self.db_session.query(self.model).filter(self.model.id == id).first()
        todo.is_completed = True
        todo.updated_at = dt.now()
        self.db_session.commit()
        self.db_session.refresh(todo)
        return todo
    
    
    async def search(self , q: str): 
        return self.db_session.query(self.model).filter(self.model.title.contains(q)).all()
    
    
    
    
    



