from marshmallow import Schema, fields


class UserAddSchema(Schema):
    email = fields.Str(required=True)


class UserGetRequestSchema(Schema):
    id_ = fields.UUID(required=True)
