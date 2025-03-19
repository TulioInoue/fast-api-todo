from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

import models
from models import Todos
from database import engine, SessionLocal
from structs import TodoRequest

app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:5173",
#     "https://frontend-vert-kappa-79.vercel.app",
#     "https://frontend-4d9vm62bd-tulio-inoues-projects.vercel.app",
#     "https://frontend-ay9u7x38r-tulio-inoues-projects.vercel.app"
#     ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Create a database
models.Base.metadata.create_all(bind = engine)

# Open and closing the database
def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()
db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/get-todos", status_code = status.HTTP_200_OK)
async def read_todos(db: db_dependency):
    return db.query(Todos).all()

@app.post("/create", status_code = status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()
    
@app.delete("/delete/{id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, id: int):

    db.query(Todos).filter(Todos.id == id).delete()
    db.commit()



