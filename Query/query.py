import strawberry
from typing import List
from outh2 import get_current_user
from repositories.blog import BlogRepository
from repositories.user import UserRepository
from strawberry_graphql_schema import GetUserType, ShowBlogType, UsersType
from strawberry.types import Info


@strawberry.type
class Query:
    @strawberry.field
    async def get_blogs(self, info: Info) -> List[ShowBlogType]:
        db = info.context['db']
        blogs = BlogRepository.get_all_blog(db)
        return blogs
    
    @strawberry.field
    async def get_blog(id: int,  info: Info) -> ShowBlogType:
        db = info.context['db']
        return BlogRepository.get_blog(db, id)
    
    @strawberry.field
    async def get_all_user(info: Info) -> List[UsersType]:
        db = info.context['db']
        return UserRepository.get_all_users(db)
    