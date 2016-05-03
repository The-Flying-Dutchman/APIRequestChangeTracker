from tracker import *
from flask import request, make_response, url_for, redirect
from tracker.models import ListModel
import json
from utils.json_util import DateTimeEncoder
from flask import render_template

list_model = ListModel()


@app.route('/list', methods=['GET'])
def list():
    return render_template('list.html')


@app.route('/get_request_lists', methods=['GET'])
def getRequestData():
    try:
        user_id = request.args.get("user_id", '').encode("utf-8")

        all_records = list_model.list_all_records(user_id)
        return make_response(json.dumps(all_records, cls=DateTimeEncoder))
    except:
        return make_response()


@app.route('/new_request', methods=['PUT'])
def new_request():
    try:
        user_id = request.form['user_id'].encode('utf-8')
        request_url = request.form['request_url'].encode('utf-8').encode('utf-8')
        request_interval = request.form['request_interval'].encode('utf-8')

        request_id = list_model.new_request(user_id, request_url, request_interval)

        return make_response(json.dumps({"request_id": request_id}), 200)
    except Exception as e:
        print e
        return make_response('{"error":"add new request fails"}', 409)


@app.route('/update_request', methods=['POST'])
def update_request():
    try:
        request_id = request.form['request_id'].encode('utf-8')
        request_url = request.form['request_url'].encode('utf-8').encode('utf-8')
        request_interval = request.form['request_interval'].encode('utf-8')
        list_model.update_request(request_id, request_url, request_interval)

        return make_response('{"success":"update success"}', 200)
    except Exception as e:
        print e
        return make_response('{"error":"update fails"}', 409)


@app.route('/delete_request', methods=['DELETE'])
def delete_request():
    try:
        request_id = request.form['request_id'].encode('utf-8')
        list_model.delete_request(request_id)
        return make_response('{"success":"delete success"}', 200)
    except Exception as e:
        print e
        return make_response('{"error":"delete fails"}', 409)