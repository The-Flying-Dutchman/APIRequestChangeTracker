from flask import request, make_response, url_for, redirect
from tracker.models.detail_model import DetailModel
from tracker import *
import json

detail_model = DetailModel()


@app.route('/detail', methods=['GET'])
def detail():
    user_id = request.args.get("request_id", '')

    request_datas = detail_model.getRequestDatas(user_id)
    return make_response(json.dumps(request_datas))
