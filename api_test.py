import json
import requests
from requests.exceptions import HTTPError
import unittest
from requests.structures import CaseInsensitiveDict


AUTH_TOKEN = ''

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer {token}".format(token=AUTH_TOKEN)

api_build_verification_test = {"home_page": "http://127.0.0.1:5000/", "settings": "http://127.0.0.1:5000/settings"}

# build verification test
# iterate through urls, test for successful requests
def api_get_smoke_test():
    for key, value in api_build_verification_test.items():
        try:
            response = requests.get(value, allow_redirects=False, headers=headers, timeout=2.50)
            response.raise_for_status()
        except HTTPError as http_err:
            # need to get the error and return the url
            print(f'HTTP error occurred: {http_err}')
            # other errors , for example failed connections
        except Exception as err:
            print(f'Other error occured: {err}')
        else:
            print(str('Success' + ' ' + key))

api_get_smoke_test()


# Run testcases test expected responses from the server
class TestUrls(unittest.TestCase):

    base_url = {"home_page ": "http://127.0.0.1:5000/"}
    AUTH_TOKEN = ''

    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer {token}".format(token=AUTH_TOKEN)

    def test_url(self):
        response = requests.get(self.base_url[""], allow_redirects=False, headers=self.headers, params={'': ''},
                            timeout=2.50)
        response_code = response.status_code
        self.assertEqual(response_code, 200, msg='error message details')


    def test_post_json(self):
        data = {'key':'value'}
        response = requests.post(self.base_url[""],data=json.dumps(data),allow_redirects=False,headers=self.headers,
                                 timeout=2.50)
        response_code = response.status_code
        # 200 (OK) or 204 (No Content) result not identified by the URI
        # 201 (Created) if a resource is recorded on the origin server
        self.assertEqual(response_code, 200, msg='error message details')


    def test_json_response(self):
        response = requests.get(self.base_url[""],allow_redirects=False, headers=self.headers, params={'':''},
                                timeout=2.50)
        data = response.json()
        response_code = response.status_code
        self.assertEqual(response_code, 200, msg='error message details')
        self.assertEqual(data['json_key'], 'expected_value',msg='error message details')


if __name__ == '__main__':
    unittest.main()
