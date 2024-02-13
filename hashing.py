from passlib.context import CryptContext

pswd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pswd_context.hash(password)
    
    def verify(hashed_password, plain_pasword):
        return pswd_context.verify(plain_pasword, hashed_password)