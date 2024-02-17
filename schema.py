
from pydantic import BaseModel
from typing import Optional

# Pydantic models
class User(BaseModel):
    username: str
    password: str

class GetUser(BaseModel):
    username: str

class Blog(BaseModel):
    title: str
    body: str
    user_id: int

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: GetUser

class Student(BaseModel):
    first_name: str
    last_name: str

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None