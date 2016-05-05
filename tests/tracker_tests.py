import os
import tracker
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_login(self):
        rv = self.login('wei', 'wei')
        print rv
        # assert 'success' in rv.data

    def test_list(self):
        self.login('wei', 'wei')
        rv = self.app.get('/get_request_lists',
                          data={"user_id":6})
        assert 'request_id' in rv.data

    def test_detail(self):
        pass

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            email=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()