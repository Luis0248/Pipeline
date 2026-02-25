import schemathesis
from schemathesis.checks import not_a_server_error
from hypothesis import settings

schema = schemathesis.openapi.from_url("https://petstore.swagger.io/v2/swagger.json")

@schema.parametrize()
# Reducimos a solo 5 ejemplos por cada método para que sea rápido
@settings(max_examples=5) 
def test_api_metodos(case):
    response = case.call()
    case.validate_response(response, checks=(not_a_server_error,))
