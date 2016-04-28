class RequestData():
    def __init__(self, data_request_id, data_content):
        self.data_request_id = data_request_id
        self.data_content = data_content

    def as_dictionary(self):
        return {"data_request_id": self.data_request_id, "data_content": self.data_content}
