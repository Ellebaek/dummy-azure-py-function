import azure.functions as func
from dummy_function01 import main
import datetime

print(datetime.datetime.now())

def test_dummy_function01():
    # Construct a mock HTTP request.
    req = func.HttpRequest(
        method='GET',
        body=None,
        url='/api/dummy_function01',
        params={'user': 'Tom'})

    # Call the function.
    resp = main(req)

    print(resp)


test_dummy_function01()
