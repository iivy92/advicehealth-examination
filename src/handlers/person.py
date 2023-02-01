from flask import Blueprint, request
from http import HTTPStatus
from src.models.schemas.person import CreatePerson
from src.use_cases.person import PersonUseCases
from src.utils.exceptions import InvalidUsage
from src.utils.authentication import auth


handler_person = Blueprint('person', __name__, url_prefix='/v1/person')


@handler_person.route('/create', methods=['POST'])
@auth.login_required
def create_person():
    try:
        dto = CreatePerson().load(request.json)
        PersonUseCases().create_person(dto)
    except Exception as e:
        raise InvalidUsage(str(e), status_code=HTTPStatus.BAD_REQUEST.value)

    return dict(result="Person sucessfully created.")


@handler_person.route('/list-owners', methods=['GET'])
@auth.login_required
def get_owners():
    try:
        owners = PersonUseCases().get_owners()
    except Exception as e:
        raise InvalidUsage(str(e), status_code=HTTPStatus.BAD_REQUEST.value)

    return dict(result=owners)


@handler_person.route('/owner/<string:document_number>', methods=['GET'])
@auth.login_required
def get_owner_by_document_number(document_number):
    try:
        owners = PersonUseCases().get_owner_by_document_number(document_number)
    except Exception as e:
        raise InvalidUsage(str(e), status_code=HTTPStatus.BAD_REQUEST.value)

    return dict(result=owners)
