class RequestRecord():
    def __init__(self, user_id, request_url, request_interval):
        self.user_id = user_id
        self.request_url = request_url
        self.request_interval = request_interval

    def as_dictionary(self):
        return {"user_id": self.user_id, "request_url": self.request_url, "request_interval": self.request_interval}
