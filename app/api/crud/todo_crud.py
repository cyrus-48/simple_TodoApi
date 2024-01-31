from app.api.models.todo import TodoCreate, TodoUpdate , TodoInDB
from app.db import todos, database  
from typing import List
from datetime import datetime as dt

class TodoCrud:
    db = None
    table = None
    def __init__(self ):
        self.db  =  database
        self.table  =  todos
        
    async def post(self , payload: TodoCreate):
        query = self.table.insert().values(
            title = payload.title,
            description = payload.description
        )
        return await self.db.execute(query)
    
    async def get_all_todos(self):
        query = self.table.select()
        return await self.db.fetch_all(query)
    
    async def get_one_todo_by_id(self , id: int):
        query = self.table.select().where(self.table.c.id == id)
        return await self.db.fetch_one(query)
    
    async def put(self , id: int , payload: TodoUpdate):
        query = self.table.update().where(self.table.c.id == id).values(
            title = payload.title,
            description = payload.description,
        )
        return await self.db.execute(query)
    
    async def delete(self , id: int):
        query = self.table.delete().where(self.table.c.id == id)
        return await self.db.execute(query)
    
    
    async def get_all_todos_completed(self):
        query = self.table.select().where(self.table.c.is_completed == True)
        return await self.db.fetch_all(query)
    
    async def get_all_todos_not_completed(self):
        query = self.table.select().where(self.table.c.is_completed == False)
        return await self.db.fetch_all(query)
    
    async def put_completed(self , id: int):
        query = self.table.update().where(self.table.c.id == id).values(
            is_completed = True,
        )
        return await self.db.execute(query)
    
    
    async def search(self , q: str):
        query = self.table.select().where(self.table.c.title.contains(q))
        return await self.db.fetch_all(query)
    
    
    
    
    



