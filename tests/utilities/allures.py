import allure
import textwrap


def print_roundtrip(response, *args, **kwargs):
    def format_headers(d): return lambda d: '\n'.join(
        f'{k}: {v}' for k, v in d.items())

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
