from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from services import get_author_id, create_author
from models import Author
from dotenv import load_dotenv
import os

load_dotenv()  

router = APIRouter()
security = HTTPBasic()

valid_users = {  
os.getenv("USER") : os.getenv("PASSWORD")
}

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
  
  if credentials.username in valid_users:
      
      stored_password = valid_users[credentials.username]
      if credentials.password == stored_password:
          return credentials.username  
  raise HTTPException(status_code=401, detail="Credenciales no válidas")


@router.post("/input/authors/{my_target_field}") 
def create_author_route(author: Author, my_target_field: str, current_user: str = Depends(get_current_user)):

  if my_target_field in ["field_1", "author", "description"]: 

    author_id = create_author(author, my_target_field)

    return {"id": author_id["id"]}
   
  return {"error": f"{my_target_field} no es un campo válido para convertir a mayúscula"}


@router.get("/authors/{id}")
def get_author_id_route(id: str):

  author = get_author_id(id)

  return {"author": author}
 
 