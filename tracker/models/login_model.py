from tracker.dao import UserDao
from tracker.models import User
import bcrypt


class LoginModel:
    def __init__(self):
        self.user_dao = UserDao()

    def create_user(self, email, password):
        user = self.user_dao.select_user_by_useremail(email)
        if user:
            return False
        else:
            user = User(email, password)
            user.password = bcrypt.hashpw(password, bcrypt.gensalt())
            self.user_dao.insert_user(user.as_dictionary())
            return True

    def login(self, email, password):
        user = self.user_dao.select_user_by_useremail(email)
        if (bcrypt.hashpw(password, user["user_password"]) == user["user_password"]):
            return True
        else:
            return False

    def get_user_info(self, email):
        user = self.user_dao.select_user_by_useremail(email)
        if not user:
            return None
        return User(user["user_email"], user["user_password"])
