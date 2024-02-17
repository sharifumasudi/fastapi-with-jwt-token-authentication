from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from hashing import Hash
import models
from repositories.user import UserRepository
from schema import GetUser, User

router = APIRouter(
    tags=["Users"],
    prefix="/user"
    ) # Initialize router

# Get all user
@router.get("/get", status_code=status.HTTP_200_OK, response_model=List[GetUser])
async def get_all_user(db: Session=Depends(get_db)):
    return UserRepository.get_all_users(db)

# Create user
@router.post("/create", status_code=status.HTTP_200_OK, response_model=GetUser)
async def create_user(request: User, db: Session = Depends(get_db)):
   return UserRepository.create_new_user(db, request)

# Get single user
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=GetUser)
async def get_user(id: int, db: Session=Depends(get_db)):
    return UserRepository.get_user(id, db)

# Delete user
@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int, db: Session=Depends(get_db)):
    return UserRepository.delete_user(db, id)