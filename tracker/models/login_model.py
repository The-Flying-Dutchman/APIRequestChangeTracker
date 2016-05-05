from tracker.dao import UserDao
from tracker.dao import User
import bcrypt


class LoginModel:
    def __init__(self):
        self.user_dao = UserDao()

    def create_user(self, email, password):
        user = self.user_dao.select_user_by_useremail(email)
        if user:
            return None
        else:
            user = User(email, password)
            user.password = bcrypt.hashpw(password, bcrypt.gensalt())
            user_id = self.user_dao.insert_user(user.as_dictionary())
            return user_id

    def login(self, email, password):
        user = self.user_dao.select_user_by_useremail(email)
        if not user: return False
        if (bcrypt.hashpw(password, user["user_password"].encode('utf-8')) == user["user_password"].encode('utf-8')):
            return True
        else:
            return False

    def get_user_info(self, email):
        user = self.user_dao.select_user_by_useremail(email)
        if not user:
            return None

        user_entity = User(user["user_email"], user["user_password"])
        user_entity.user_id = user["user_id"]
        user_entity.id = user["user_email"]
        return user_entity
