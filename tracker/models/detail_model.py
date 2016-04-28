from tracker.dao import RequestDataDao
from tracker.dao import RequestRecordDao


class DetailModel:
    def __init__(self):
        self.request_data_dao = RequestDataDao()

    def getRequestDatas(self, request_id):
        return self.request_data_dao.select_request_data_by_requestid(request_id)

    def getRequestDataDetail(self, data_id):
        return self.request_data_dao.select_request_data_by_requestid(data_id)
