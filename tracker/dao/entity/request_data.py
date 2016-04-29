class RequestData():
    def __init__(self, data_request_id, data_content):
        self.data_request_id = data_request_id.encode("utf-8")
        self.data_content = data_content.encode("utf-8")

    def as_dictionary(self):
        return {"data_request_id": self.data_request_id, "data_content": self.data_content}
