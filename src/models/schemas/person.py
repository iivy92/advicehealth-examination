from marshmallow import Schema, fields


class CreatePerson(Schema):
    name = fields.String(required=True)
    document_number = fields.String(required=True)
