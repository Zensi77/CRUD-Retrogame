from passlib.context import CryptContext
pwdContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    @staticmethod
    def verifyPassword(plain_password, hashed_password):
        return pwdContext.verify(plain_password, hashed_password)
    @staticmethod
    def getPasswordHash(password):
        return pwdContext.hash(password)