from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
import models
from outh2 import get_current_user
from repositories.blog import BlogRepository
from schemas import Blog, ShowBlog, User

router = APIRouter(
    tags=['Blogs'],
    prefix="/blog",
    # dependencies=[Depends()]
)

@router.get("/all",status_code=200, response_model=List[ShowBlog])
async def get_blog(get_current_user: User = Depends(get_current_user), db: SessionLocal = Depends(get_db)):
    return BlogRepository.get_all_blog(db)

@router.post("/create", status_code=201)
def create_blog(request: Blog, get_current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
   return BlogRepository.create_blog_post(db, request)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowBlog)
async def get_blog(id: int,  response: Response, get_current_user: User = Depends(get_current_user), db: Session=Depends(get_db)):
    return BlogRepository.get_blog(db, id)

@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(id: int, response: Response, get_current_user: User = Depends(get_current_user), db: Session=Depends(get_db)):
    return BlogRepository.delete_blog(db, id, response)


@router.put("/{id}/update", status_code=status.HTTP_202_ACCEPTED)
async def update_blog(id: int, request: Blog, response: Response, get_current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
 return BlogRepository.update_blog(db, id, request, response)