import flask.ext.login as flask_login

class User(flask_login.UserMixin):

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.id = email

    def as_dictionary(self):
        return {"email": self.email, "password": self.password}
