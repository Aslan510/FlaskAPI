import unittest
import requests

url = 'http://localhost'

class TestAPI(unittest.TestCase):

    def test_md5(self):
        json_data = requests.get(url+"/md5/test")
        result = 
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
