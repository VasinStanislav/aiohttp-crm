from marshmallow import Schema, fields
from app.crm.schemes import UserAddSchema


class OkResponseSchema(Schema):
    status = fields.Str()
    data = fields.Dict()


class UserSchema(UserAddSchema):
    id_ = fields.UUID(required=True)


class ListUsersSchema(Schema):
    users = fields.Nested(UserSchema, many=True)


class ListUsersResponseSchema(OkResponseSchema):
    data = fields.Nested(ListUsersSchema)


class UserGetSchema(Schema):
    user = fields.Nested(UserSchema)


class UserGetResponseSchema(OkResponseSchema):
    data = fields.Nested(UserGetSchema)
