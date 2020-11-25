import json
import unittest

from main import app


class FlaskTest(unittest.TestCase):

    def test_first(self):
        tester = app.test_client(self)
        app.config['TESTING'] = True
        res = tester.get('/users')
        data = res.data.decode('utf8').replace("'", '"')
        data = json.loads(data)

        # for fail this test
        # data['test_user']['id'] = 1

        expected_output = {"test_user": {"name": "Test User", "favorite_color": "Black"}}
        self.assertEqual(data, expected_output)

    def test_second(self):
        tester = app.test_client(self)
        app.config['TESTING'] = True

        res = tester.get('/users/test_user')
        data = res.data.decode('utf8').replace("'", '"')
        data = json.loads(data)

        expected_output = {"test_user": {"id": "test", "name": "Test User", "favorite_color": "Black"}}
        self.assertEqual(data, expected_output)

    def test_third(self):
        tester = app.test_client(self)
        app.config['TESTING'] = True

        res = tester.get('/users/user1234')
        data = res.data.decode('utf8').replace("'", '"')

        expected_output = 'user does not exist in the database'
        self.assertEqual(data, expected_output)
        self.assertEqual(res.status_code, 404)


if __name__ == '__main__':
    unittest.main()
