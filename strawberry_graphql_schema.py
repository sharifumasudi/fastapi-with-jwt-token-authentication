# Strawberry types
from typing import Optional
import strawberry


@strawberry.type
class UserType:
    username: str
    password: str

@strawberry.type  
class UsersType():
    username: str

@strawberry.input  
class UserTypeInput():
    username: str
    password: str

@strawberry.type
class GetUserType:
    username: str

@strawberry.type
class BlogType:
    title: str
    body: str
    user_id: int

@strawberry.type
class ShowBlogType:
    title: str
    body: str
    creator: GetUserType

@strawberry.type
class StudentType:
    first_name: str
    last_name: str

@strawberry.type
class LoginType:
    username: str
    password: str

@strawberry.type
class TokenType:
    access_token: str
    token_type: str

@strawberry.type
class TokenDataType:
    username: Optional[str] = None