
import requests
from behave import given, when, then, step
from tests.utilities.logs import create_logger
from tests.rests.rest_client import PetStoreAPIClient


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


@when("test GET get_store_inventory api")
def step_impl(context):
    api_client = PetStoreAPIClient()
    response = api_client.get_store_inventory()
    context.response = response


@then("the response code is equal to {status_code}")
def step_impl(context, status_code):
    response = context.response
    assert response.status_code == int(status_code)
