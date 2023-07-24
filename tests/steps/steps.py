from behave import given, when, then
import requests
import json
import pprint


@given("Hello World1")
def step_impl(context):
    print("11111111")
    print("22222222")
    print("33333333")


@when("Hello1")
def step_impl(context):
    print("44444444")


@given("test request")
def step_impl(context):
    response = requests.get("https://petstore.swagger.io/v2/store/inventory")
    pprint.pprint(response.json())


@given("Number is {number}")
def step_impl(context, number):
    print(number)
    context.number = number


@when("show number from context")
def step_impl(context):
    print(context.number)