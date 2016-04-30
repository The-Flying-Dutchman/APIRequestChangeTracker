from flask import request, make_response, render_template, redirect
from tracker.models.detail_model import DetailModel
from tracker import *
import json
from utils.json_util import DateTimeEncoder
detail_model = DetailModel()


@app.route('/detail', methods=['GET'])
def detail():
     return render_template('detail.html')

@app.route('/get_request_details', methods=['GET'])
def getRequestChanges():
    request_id = request.args.get("request_id", '').encode("utf-8")

    request_datas = detail_model.getRequestDatas(request_id)
    return make_response(json.dumps(request_datas, cls=DateTimeEncoder))
