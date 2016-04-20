from com.tracker.dao.request_info_dao import RequestInfoDao;

class RequestInfo:

    def __init__(self):
        request_info_dao = RequestInfoDao()

    def add_request_info(self, request_info):
        self.request_info_dao.insert_request_info(request_info)
