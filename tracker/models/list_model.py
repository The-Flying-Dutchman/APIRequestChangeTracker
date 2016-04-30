from tracker.dao import RequestDataDao
from tracker.dao import RequestRecordDao
from tracker.dao import RequestRecord
from tracker.dao import RequestData
import requests

import json
from datetime import datetime


class ListModel:
    def __init__(self):
        self.request_record_dao = RequestRecordDao()
        self.request_data_dao = RequestDataDao()

    def get_data_from_url(self, request_url):
        resp = requests.get(request_url)
        return resp.text

    def new_request(self, user_id, request_url, request_interval):
        try:
            request_record = RequestRecord(user_id, request_url, request_interval)
            request_id = self.request_record_dao.insert_request_record(request_record.as_dictionary())

            data_content = self.get_data_from_url(request_url)

            request_data = RequestData(request_id, data_content)
            self.request_data_dao.insert_request_data(request_data.as_dictionary())

            return request_id
        except:
            return 0

    def list_all_records(self, user_id):
        try:
            results = self.request_record_dao.select_request_record_by_userid(user_id)
            return results

        except:
            return None

    def update_request(self, request_id, request_url, request_interval):
        try:

            request_record = {"request_id": request_id, "request_url": request_url,
                              "request_interval": request_interval}

            return True if self.request_record_dao.update_request(request_record) else False

        except:
            return False


    def delete_request(self, request_id):
        try:
            self.request_record_dao.delete_request_by_requestid(request_id)
            self.request_data_dao.select_request_data_by_requestid(request_id)
            return True
        except:
            return False