from fastapi import APIRouter, Depends, HTTPException , status ,Path
from  fastapi.encoders import jsonable_encoder
from app.api.models.todo import TodoCreate, TodoUpdate , TodoInDB
from app.api.crud.todo_crud import TodoCrud
from typing import List 

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)
@router.get("/test")
async def test_route():
    return {"test":"test"}
@router.post("/", response_model=TodoInDB, status_code=status.HTTP_201_CREATED)
async def create_todo( payload: TodoCreate, todo_crud: TodoCrud = Depends(),):
    todo = await todo_crud.post(payload)    
    return TodoInDB(**jsonable_encoder(todo))
    

@router.get("/", response_model=List[TodoInDB])
async def read_all_todos(todo_crud: TodoCrud = Depends()):
    todos = await todo_crud.get_all_todos()
    return todos

@router.get("/completed", response_model=List[TodoInDB])
async def read_all_todos_completed(todo_crud: TodoCrud = Depends()):
    todos = await todo_crud.get_all_todos_completed()
    return todos

@router.get("/not_completed", response_model=List[TodoInDB])
async def read_all_todos_not_completed(todo_crud: TodoCrud = Depends()):
    todos = await todo_crud.get_all_todos_not_completed()
    return todos

@router.get("/{id}", response_model=TodoInDB)
async def read_one_todo_by_id(id: int = Path(..., gt=0), todo_crud: TodoCrud = Depends()):
    todo = await todo_crud.get_one_todo_by_id(id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{id}", response_model=TodoInDB)
async def update_todo_by_id(id: int = Path(..., gt=0), payload: TodoUpdate = Depends(), todo_crud: TodoCrud = Depends(),):
    todo = await todo_crud.get_one_todo_by_id(id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo = await todo_crud.put(id, payload)
    return TodoInDB(**payload.dict(), id=id)

@router.put("/completed/{id}", )
async def update_todo_completed_by_id(id: int = Path(..., gt=0), todo_crud: TodoCrud = Depends(),):
    ''' Change todo status to completed'''
    todo = await todo_crud.get_one_todo_by_id(id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo = await todo_crud.put_completed(id)
    return  {"message": "Todo updated successfully"}

@router.get("/search/{q}", response_model=List[TodoInDB])
async def search(q: str = Path(..., min_length=3), todo_crud: TodoCrud = Depends(),):
    ''' Search todo by title '''
    todos = await todo_crud.search(q)
    return todos

@router.delete("/{id}" )
async def delete_todo_by_id(id: int = Path(..., gt=0), todo_crud: TodoCrud = Depends(),):
    todo = await todo_crud.get_one_todo_by_id(id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo = await todo_crud.delete(id)
    return {"message": "Todo deleted successfully"}