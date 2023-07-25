
import requests
import pprint
from behave import given, when, then, step
from tests.utilities.logs import create_logger

logger = create_logger(__name__)


@given("This is Given statement")
def step_impl(context):
    print('This is Given Statement')


@when("This is When statement")
def step_impl(context):
    print('This is When Statement')


@then("This is Then statement")
def step_impl(context):
    print('This is Then statement')


@step("This is Given statement start from step")
def step_impl(context):
    print('This is When statement start from step')


@step("This is When statement start from step")
def step_impl(context):
    print('This is When statement start from step')


@step("This is Then statement start from step")
def step_impl(context):
    print('This is Then statement start from step')


@step("Set Number to {number}")
def step_impl(context, number):
    print(f'Number is {number}')


@given("Set a storage to context")
def step_impl(context):
    context.storage = {}


@when("Set Number to {number} and store to storage[{key}]")
def step_impl(context, number, key):
    print(f'Number is {number}')
    context.storage[key] = number


@when("Get Number from storage[{key}]")
def step_impl(context, key):
    print(f'Number is {context.storage[key]}')


@step("This is the root statement")
def step_impl(context):
    print('This is the root statement')
    steps = ['Given This is the secondary layer statement']
    context.execute_steps('\n'.join(steps))


@step("This is the secondary layer statement")
def step_impl(context):
    print('This is the root statement')


@given("test request")
def step_impl(context):
    response = requests.get(
        "https://petstore.swagger.io/v2/store/inventory")
    # pprint.pprint(response.json())
