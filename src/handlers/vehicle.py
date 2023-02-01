from flask import Blueprint, request
from http import HTTPStatus
from src.models.schemas.vehicle import AssignVehicle
from src.use_cases.vehicle import VeihicleUseCases
from src.utils.exceptions import InvalidUsage
from src.utils.authentication import auth


handler_vehicle = Blueprint('vehicle', __name__, url_prefix='/v1/vehicle')


@handler_vehicle.route('/assign', methods=['POST'])
@auth.login_required
def assing_vehicle():
    try:
        dto = AssignVehicle().load(request.json)
        veihicle_assigned = VeihicleUseCases().assign_veihicle(dto)
        return dict(result="Veihicle sucessfully assigned to owner")
    except Exception as e:
        raise InvalidUsage(str(e), status_code=HTTPStatus.BAD_REQUEST.value)
