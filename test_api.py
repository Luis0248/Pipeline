import schemathesis
from schemathesis.checks import not_a_server_error

schema = schemathesis.openapi.from_url("https://petstore.swagger.io/v2/swagger.json")

@schema.parametrize()
def test_api_metodos(case):
    response = case.call()
    
    case.validate_response(response, checks=(not_a_server_error,))