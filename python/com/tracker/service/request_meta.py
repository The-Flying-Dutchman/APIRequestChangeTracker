from com.tracker.dao.request_meta_dao import RequestMetaDao

class RequestMeta:

    def __init__(self):
        self.request_meta_dao = RequestMetaDao()

    def add_new_request_meta(self, request_meta):
        self.request_meta_dao.insert_request_meta(request_meta)
