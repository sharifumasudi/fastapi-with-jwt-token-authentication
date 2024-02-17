from datetime import timedelta
from JWTtoken import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from database import get_db
from hashing import Hash
import models
from fastapi import HTTPException, status

from schema import Token

class UserRepository():
    def get_all_users(db):
        users = db.query(models.User).all()
        return users
    
    def create_new_user(db, request):
        user = db.query(models.User).filter(models.User.username == request.username).first()
        if not user:
            user = models.User(username=request.username, password=Hash.bcrypt(request.password))
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        return {"msg" : "User already registered!"}
    
    def get_user(id, db):
        user = db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found brother")
        return user
    
    def delete_user(db, id: int):
        user = db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User to delete not found!")
        db.delete(user)
        db.commit()
        return {"msg" : "User deleted successfully!"}
    
    def user_login(db, request):
        user = db.query(models.User).filter(models.User.username == request.username).first()
        if not user:
            raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Incorrect username or password",
                        headers={"WWW-Authenticate": "Bearer"},
                    )
        if not Hash.verify(user.password, request.password):
            raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Incorrect username or password",
                        headers={"WWW-Authenticate": "Bearer"},
                    )  
        # Generate JWT token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return Token(access_token=access_token, token_type="bearer")