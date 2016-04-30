from tracker import *
from flask import url_for, redirect, render_template


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')