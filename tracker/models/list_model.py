from tracker.dao import RequestDataDao
from tracker.dao import RequestRecordDao
from tracker.dao import RequestRecord
from tracker.dao import RequestData
import requests


class ListModel:
    def __init__(self):
        self.request_record_dao = RequestRecordDao()
        self.request_data_dao = RequestDataDao()

    def get_data_from_url(self, url):
        resp = requests.get(url)
        return resp.text()

    def new_track(self, user_id, url, interval):
        try:
            request_record = RequestRecord(user_id, url, interval)
            request_id = self.request_record_dao.insert_request_record(request_record.as_dictionary())

            data_content = self.get_data_from_url(url)

            request_data = RequestData(request_id, data_content)
            self.request_data_dao.insert_request_data(request_data.as_dictionary())

            return True
        except:
            return False

    def list_all_records(self, user_id):
        try:
            return self.request_record_dao.select_request_record_by_userid(user_id)
        except:
            return None
