import strawberry

from Mutation.mutations import BlogMutation, UserLoginMutation


@strawberry.type
class Mutation(BlogMutation, UserLoginMutation):
    ...