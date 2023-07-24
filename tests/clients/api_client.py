import requests
from tests.utilities.allures import print_roundtrip


class APIClient:

    def __init__(self):
        self._session = requests.session()
        self._baseURL = "https://petstore.swagger.io"

    def get(self, uri, params):
        self._session.get(f'{self._baseURL}/{uri}',
                          params=params, hooks={'response': print_roundtrip})

    def put(self, uri, json, data):
        self._session.put(f'{self._baseURL}/{uri}', json=json,
                          data=data, hooks={'response': print_roundtrip})

    def post(self, uri, json, data):
        self._session.post(f'{self._baseURL}/{uri}', json=json,
                           data=data, hooks={'response': print_roundtrip})

    def delete(self, uri, json):
        self._session.delete(f'{self._baseURL}/{uri}',
                             json=json, hooks={'response': print_roundtrip})
