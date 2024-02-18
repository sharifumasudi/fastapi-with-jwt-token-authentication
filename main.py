from fastapi import FastAPI
from Mutation.collection_of_mutations import Mutation
from Mutation.mutations import BlogMutation
import models
from database import engine
from strawberry.fastapi import GraphQLRouter
import strawberry
from strawberry.asgi import GraphQL
from routers import blogs, login, users
from strawberry_graphql_schema import UserType, GetUserType, BlogType, ShowBlogType, StudentType, LoginType, TokenType, TokenDataType
from Context.context import get_context
from Query.query import Query

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get('/', tags=["API's"])
async def index():
    return "Welcome back!"
app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(login.router)
# Create GraphQL schema using Strawberry
schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    types=[
    UserType, 
    GetUserType, 
    BlogType, 
    ShowBlogType,
    StudentType,
    LoginType, 
    TokenType, 
    TokenDataType])

# Create GraphQL route using GraphQLApp
graphql_app = GraphQLRouter(schema, context_getter=get_context)

# Register GraphQL route
app.include_router(graphql_app, prefix="/graphql")