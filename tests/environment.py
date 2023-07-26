import allure
from dotenv import load_dotenv
from behave import fixture, use_fixture
from swagger_coverage_py.reporter import CoverageReporter

load_dotenv(".env")

# @fixture
# def foo(context):
#     print("Hi")


def before_all(context):
    reporter = CoverageReporter(api_name="petstore", host="https://petstore.swagger.io")
    reporter.cleanup_input_files()
    reporter.setup(path_to_swagger_json="/v2/swagger.json")
    context.reporter = reporter


def after_all(context):
    reporter = context.reporter
    reporter.generate_report()


def after_step(context, step):
    stdout = context.stdout_capture.getvalue()
    stderr = context.stderr_capture.getvalue()
    if stdout:
        allure.attach(
            stdout, name="stdout", attachment_type=allure.attachment_type.TEXT
        )
    if stderr:
        allure.attach(
            stderr, name="stderr", attachment_type=allure.attachment_type.TEXT
        )
