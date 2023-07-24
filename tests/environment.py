from behave import fixture, use_fixture
import allure

@fixture
def foo(context):
    print("Hi")


def before_all(context):
    print("This is before all")
    print("This is before all")
    print("This is before all")
    use_fixture(foo, context)

def after_scenario(context, scenario):
    stdout = context.stdout_capture.getvalue()
    stderr = context.stderr_capture.getvalue()
    if stdout:
        allure.attach(stdout, name="stdout", attachment_type=allure.attachment_type.TEXT)
    if stderr:
        allure.attach(stderr, name="stderr", attachment_type=allure.attachment_type.TEXT)