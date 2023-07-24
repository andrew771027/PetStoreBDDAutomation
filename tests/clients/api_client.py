import requests
import textwrap
import allure


def print_roundtrip(response, *args, **kwargs):
    def format_headers(d):
        return '\n'.join(f'{k}: {v}' for k, v in d.items())

    log = textwrap.dedent('''
        ---------------- request ----------------
        {req.method} {req.url}
        {reqhdrs}

        {req.body}
        ---------------- response ----------------
        {res.status_code} {res.reason} {res.url}
        {reshdrs}

        {res.text}
    ''').format(
        req=response.request,
        res=response,
        reqhdrs=format_headers(response.request.headers),
        reshdrs=format_headers(response.headers),
    )

    allure.attach(f"{log}", "Log", allure.attachment_type.TEXT)

# requests.get('https://httpbin.org/', hooks={'response': print_roundtrip})


class APIClient:

    def __init__(self):
        self._session = requests.session()
        self._baseURL = "https://petstore.swagger.io"

    def get(self, uri, params):
        self._session.get(f'{self._baseURL}/{uri}', params=params)

    def put(self, uri, json, data):
        self._session.put(f'{self._baseURL}/{uri}', json=json, data=data)

    def post(self, uri, json, data):
        self._session.post(f'{self._baseURL}/{uri}', json=json, data=data)

    def delete(self, uri, json):
        self._session.delete(f'{self._baseURL}/{uri}', json=json)
