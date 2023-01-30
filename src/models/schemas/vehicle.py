from marshmallow import Schema, fields, validate
from enum import Enum


class Colors(Enum):
    YELLOW = "yellow"
    BLUE = "blue"
    GRAY = "gray"


class Models(Enum):
    HATCH = "hatch"
    SEDAN = "sedan"
    CONVERTIBLE = "convertible"


class AssignVehicle(Schema):
    license_plate = fields.String(required=True)
    color = fields.String(required=True, validate=validate.OneOf([color.value for color in Colors]))
    model = fields.String(required=True, validate=validate.OneOf([model.value for model in Models]))
    owner_id = fields.Integer(required=True)


