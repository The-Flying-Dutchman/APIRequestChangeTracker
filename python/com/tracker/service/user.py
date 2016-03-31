from com.tracker.dao.user_dao import userDao;

class User:

    def __init__(self):
        user_dao = userDao()
        message = {"result": ""}

    def register(self, username, password):
        user = self.user_dao.select_user_by_username(username)
        if not user:
            self.message["result"] = "Your username has been used."
            return self.message
        else:
            user = {"username": username, "password": password};
            self.user_dao.insert_user(user)
            self.message["result"] = "Create account success."
            return self.message

    def login(self, username, password):
        user = self.user_dao.select_user_by_username(username)
        if user["password"] == password:
            self.message["result"] = "Login success"
        else:
            self.message["result"] = "Login failure"
        return self.message
