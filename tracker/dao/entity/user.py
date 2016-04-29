import flask.ext.login as flask_login


class User(flask_login.UserMixin):
    def __init__(self, email, password):
        self.email = email.encode("utf-8")
        self.password = password.encode("utf-8")
        self.id = email.encode("utf-8")
        self.user_id =None

    def as_dictionary(self):
        return {"email": self.email, "password": self.password}
