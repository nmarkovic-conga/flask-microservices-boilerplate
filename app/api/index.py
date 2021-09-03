from flask import (
    Blueprint
)
from app.api.utils import response


test_response = [{
    'id': 1,
    'message': 'Hello'
}]

index = Blueprint(name='index', import_name=__name__, url_prefix="/v1")


@index.route('/test', methods=['GET'])
def test_result():
    return response(200, test_response)
