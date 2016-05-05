import unittest
import requests


class TrackerTestCase(unittest.TestCase):
    def setUp(self):
        self.URL = "http://localhost:5000"

    def test_login(self):
        rv = self.login('test@gmail', '123456')
        print rv
        assert 'success' in rv.content

    def test_list_apis(self):
        self.login('test@gmail', '123456')
        rv = requests.get(self.URL + "/get_request_lists?user_id=28")
        assert 'request_id' in rv.content

        rv = requests.put(self.URL + "/new_request", data=dict(
                user_id="1",
                request_url="https://pages.github.com/versions.json",
                request_interval=2
        ))
        assert 'request_id' in rv.content

        rv = requests.put(self.URL + "/update_request", data=dict(
                request_id=1,
                request_url="https://pages.github.com/versions.json",
                request_interval=3
        ))
        assert 'success' in rv.content

    def test_detail(self):
        self.login('test@gmail', '123456')
        rv = requests.get(self.URL + '/get_request_details?request_id=2')
        assert 'request_id' in rv.content

    def login(self, email, password):
        return requests.post(self.URL + '/login', data=dict(
                email=email,
                password=password
        ))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
