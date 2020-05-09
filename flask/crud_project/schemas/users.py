from marshmallow import Schema, fields


class UserSchema(Schema):
    email = fields.Email()
    first_name = fields.Str()
    last_name = fields.Str()
