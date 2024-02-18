import typing

from strawberry.permission import BasePermission
from strawberry.types import Info
from outh2 import get_current_user

class IsAuthenticated(BasePermission):
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request = info.context['request']
        authentication = request.headers["Authorization"]
        if authentication:
            token = authentication.split("Bearer ")[-1]
            return get_current_user(token)
        return False