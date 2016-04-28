from tracker import *
from flask import url_for, redirect


@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))