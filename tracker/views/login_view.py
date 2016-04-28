from tracker import *
import flask.ext.login as flask_login
from flask import request, make_response, url_for, redirect
from tracker.models.login_model import LoginModel
import bcrypt

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

login_model = LoginModel()


@app.route("/register", methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return '''
               <form action='create' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'></input>
                <input type='password' name='password' id='password' placeholder='password'></input>
                <input type='submit' name='submit'></input>
               </form>
               '''
    email = request.form['email'].encode("utf-8")
    password = request.form['password'].encode("utf-8")

    if login_model.create_user(email, password):
        user = login_model.get_user_info(email)
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))
    else:
        return make_response('{"error":"Email already exists in the system"}', 409)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'></input>
                <input type='password' name='password' id='password' placeholder='password'></input>
                <input type='submit' name='submit'></input>
               </form>
               '''
    email = request.form['email'].encode("utf-8")
    password = request.form['password'].encode("utf-8")

    if login_model.login(email, password):
        user = login_model.get_user_info(email)
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return make_response('{"error":"Email and password doesn\'t match"}', 409)


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
    email = request.form.get('email').encode("utf-8")

    user = login_model.get_user_info(email)

    if not user:
        return
    password = request.form.get("password").encode("utf-8")
    user.is_authenticated = bcrypt.hashpw(password, user.password) == user.password

    return user
