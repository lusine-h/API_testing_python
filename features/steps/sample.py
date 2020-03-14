from behave import *
import requests
import json

api_endpoints = {}
request_headers = {}

@then("I receive valid HTTP response code {response_code}")
def step_impl(context, response_code):
    """
    :type response_code: str
    :type context: behave.runner.Context
    """
    if context.response.__getattribute__("status_code"):
        print("\nThe response code is: {}".format(context.response.status_code))
        assert context.response.status_code is int(response_code)

@given("I set REST API base URL")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global api_url
    api_url = "http://jsonplaceholder.typicode.com"


@given("I set GET request endpoint")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    api_endpoints["GET_URL"] = api_url + "/albums"
    print("URL is: {}".format(api_endpoints["GET_URL"]))


@step('set Header content type parameter as "{content_type}"')
def step_impl(context, content_type):
    """
    :type content_type: str
    :type context: behave.runner.Context
    """
    request_headers['Content-Type'] = content_type
    print("The headers are:\n", request_headers)


@when("I make a GET request")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    response = requests.get(
        url=api_endpoints["GET_URL"], headers=request_headers
    )
    context.response = response
    print("\nThe response text is:", response.text)


@step("the GET request response type is JSON")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    content_type = context.response.headers.get("Content-Type", None)
    assert 'json' in content_type, "Content type is not JSON"




@step("the response parameter title contains {string}")
def step_impl(context, string):
    """
    :type string: str
    :type context: behave.runner.Context
    """
    response2json = json.loads(context.response.text)
    assert string in response2json['title'], "title does not contain {}".format(string)

# @step("the response contains 5 ids")
# def step_impl(context):
#     response2json = json.loads(context.response.text)
#     assert response2json[0]['id'] == 1, "aaaaaaaaaa"
#     ids = [element['id'] for element in response2json]
#     print(ids)
#     print(len(ids))
#     emails = [element['email'] for element in response2json]
#     i = 0
#     while i < len(emails):
#          print(emails[i])
#          i += 2

@step("print the response parameter title contains qui")
def step_impl(context):
    response2json = json.loads(context.response.text)
    titles = [element['title'] for element in response2json]
    for element in titles:
        if "qui" in element:
            print(element)