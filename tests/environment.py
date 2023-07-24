from __future__ import print_function
from behave import fixture, use_fixture


@fixture
def foo(context):
    print("Hi")


def before_all(context):
    print("This is before all")
    print("This is before all")
    print("This is before all")
    use_fixture(foo, context)
