import requests


class APIClient:

    def __init__(self):
        self._session = requests.session()
        self._baseURL = "https://petstore.swagger.io"

    def get(self, uri):
        self._session.get(f'{self._baseURL}/{uri}')
