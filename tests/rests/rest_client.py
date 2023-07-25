import requests
from tests.utilities.allures import print_roundtrip
from tests.rests.endpoints import PetStoreEndpointMixin


class PetStoreAPIClient(PetStoreEndpointMixin):

    def __init__(self):
        self.client = requests.session()
        self._base_url = "https://petstore.swagger.io"

    def get(self, path: str, params=None):
        resp = self.client.get(f'{self._base_url}{path}',
                               params=params,
                               hooks={'response': print_roundtrip})
        return resp

    def patch(self, path: str, headers=None, data=None, json=None):
        resp = self.client.patch(f'{self._base_url}{path}',
                                 headers=headers,
                                 json=json,
                                 data=data,
                                 hooks={'response': print_roundtrip})
        return resp

    def post(self, path: str, headers=None, data=None, json=None, files=None):
        resp = self.client.post(f'{self._base_url}{path}',
                                headers=headers,
                                json=json,
                                data=data,
                                files=files,
                                hooks={'response': print_roundtrip})
        return resp

    def delete(self, path: str, params=None):
        resp = self.client.delete(f'{self._base_url}{path}',
                                  params=params,
                                  hooks={'response': print_roundtrip})
        return resp
