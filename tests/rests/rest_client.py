import requests
from tests.utilities.allures import print_roundtrip
from tests.rests.endpoints import PetStoreEndpointMixin
from swagger_coverage_py.listener import CoverageListener
from requests.auth import HTTPBasicAuth


class PetStoreAPIClient(PetStoreEndpointMixin):
    def __init__(self):
        self.client = requests.session()
        self._base_url = "https://petstore.swagger.io"

    def get(self, path: str, uri_params: dict = None, params: dict = None):
        response = CoverageListener(
            method="get",
            base_url=self._base_url,
            raw_path=path,
            uri_params=uri_params if uri_params else dict(),
            auth=HTTPBasicAuth("username", "password"),
            params=params if params else dict(),
        ).response

        # resp = self.client.get(f'{self._base_url}{path}',
        #                        params=params,
        #                        hooks={'response': print_roundtrip})
        return response

    def patch(self, path: str, headers=None, data=None, json=None):
        resp = self.client.patch(
            f"{self._base_url}{path}",
            headers=headers,
            json=json,
            data=data,
            hooks={"response": print_roundtrip},
        )
        return resp

    def post(self, path: str, headers=None, data=None, json=None, files=None):
        resp = self.client.post(
            f"{self._base_url}{path}",
            headers=headers,
            json=json,
            data=data,
            files=files,
            hooks={"response": print_roundtrip},
        )
        return resp

    def delete(self, path: str, params=None):
        resp = self.client.delete(
            f"{self._base_url}{path}",
            params=params,
            hooks={"response": print_roundtrip},
        )
        return resp
