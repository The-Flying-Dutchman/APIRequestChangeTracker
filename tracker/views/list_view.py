from tracker import *
from flask import request, make_response, url_for, redirect
from tracker.models import ListModel
import json

list_model = ListModel()


@app.route('/list', methods=['GET'])
def list():
    user_id = request.args.get("user_id", '')

    all_records = list_model.list_all_records(user_id)
    return make_response(json.dumps(all_records))


@app.route('/new_track', methods=['POST'])
def new_track():
    user_id = request.form('user_id').encode('utf-8')
    url = request.form['url'].encode('utf-8').encode('utf-8')
    interval = request.form['interval_hour'].encode('utf-8')

    if list_model.new_track(user_id, url, interval):
        return redirect(url_for('list', user_id=user_id))
    else:
        return make_response('{"error":"add new request fails"}', 409)
