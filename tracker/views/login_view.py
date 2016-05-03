from tracker import *
import flask.ext.login as flask_login
from flask import request, make_response, url_for, redirect
from tracker.models.login_model import LoginModel
import bcrypt

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

login_model = LoginModel()


@app.route("/register", methods=['POST'])
def create_user():
    try:
        email = request.form['email'].encode("utf-8")
        password = request.form['password'].encode("utf-8")

        user_id = login_model.create_user(email, password)
        user = login_model.get_user_info(email)
        user.id = email
        user.user_id = user_id

        flask_login.login_user(user)
        return redirect(url_for('list'))
    except:
        return make_response('{"error":"Email already exists in the system"}', 409)


@app.route('/login', methods=['POST'])
def login():
    try:
        email = request.form['email'].encode("utf-8")
        password = request.form['password'].encode("utf-8")

        if login_model.login(email, password):
            user = login_model.get_user_info(email)
            flask_login.login_user(user)
            return redirect(url_for('list'))
    except:
        make_response('{"error":"Email and password doesn\'t match"}', 409)



@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('/'))


@login_manager.user_loader
def user_loader(email):
    user = login_model.get_user_info(email)
    if not user:
        return

    return user


@login_manager.request_loader
def request_loader(request):
    try:
        email = request.form.get('email').encode("utf-8")

        user = login_model.get_user_info(email)

        if not user:
            return
        password = request.form.get("password").encode("utf-8")
        user.is_authenticated = bcrypt.hashpw(password, user.password) == user.password

        return user
    except:
        return
