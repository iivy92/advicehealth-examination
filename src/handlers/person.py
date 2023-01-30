from flask import Blueprint, request
from http import HTTPStatus
from src.models.schemas.person import CreatePerson
from src.use_cases.person import PersonUseCases
from src.utils.exceptions import InvalidUsage

handler_person = Blueprint('person', __name__, url_prefix='/v1/person')

@handler_person.route('/create', methods=['POST'])
def create_person():
    try:
        dto = CreatePerson().load(request.json)
        created_person = PersonUseCases().create_person(dto)
    except Exception as e:
        raise InvalidUsage(str(e), status_code=HTTPStatus.BAD_REQUEST.value)

    return dict(result="Person sucessfully created.")
    
