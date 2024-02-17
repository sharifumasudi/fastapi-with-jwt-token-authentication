
from datetime import timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import strawberry
from strawberry.types import Info
from JWTtoken import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from hashing import Hash
import models
from repositories.blog import BlogRepository
from repositories.user import UserRepository
from strawberry_graphql_schema import ShowBlogType, TokenType, UserType


@strawberry.input
class RegisterBlogInput:
    title: str
    body: str
    user_id: int

@strawberry.input
class UpdateBlogInput:
    title: str
    body: str

@strawberry.input
class UserInputType:
    username: str
    password: str
    
@strawberry.type
class BlogMutation:
    @strawberry.mutation
    def create_blog(self, request: RegisterBlogInput, info: Info) -> ShowBlogType:
        db = info.context['db']
        return BlogRepository.create_blog_post(db, request)
    
    @strawberry.mutation
    async def delete_blog(id: int, info: Info) -> str:
        db = info.context['db']
        return BlogRepository.delete_blog(db, id)
    
    @strawberry.mutation
    async def update_blog(id: int, request: UpdateBlogInput, info: Info) -> str:
        db = info.context['db']
        return BlogRepository.update_blog(db, id, request)
    
@strawberry.type
class UserLoginMutation:
    @strawberry.mutation
    async def login(info: Info, request: UserInputType) -> TokenType:
        db = info.context['db']
        return UserRepository.user_login(db, request)