from fastapi import Depends, Request
from sqlalchemy.orm import Session
from outh2 import get_current_user
from database import get_db
from schema import User


async def get_context(request: Request, db: Session = Depends(get_db)):
    return {
        'db': db,
    }