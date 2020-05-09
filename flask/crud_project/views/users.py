from flask import Blueprint, request
from marshmallow import ValidationError

from schemas.users import UserSchema
from models.users import UserModel

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/')
def hello():
    return "Hello World!"


@user_blueprint.route('/user_list/')
def user_list():
    return {"user_list": UserSchema(many=True).dump(UserModel.scan())}


@user_blueprint.route('/user_create/', methods=['POST'])
def user_create():
    error = None
    data = request.json
    try:
        data = UserSchema().load(request.json)
    except ValidationError as err:
        error = err
    if not error:
        user = UserModel(**data)
        user.save()
    return {
        "status": "error" if error else "success",
        "error": error,
        "data": data
    }


@user_blueprint.route('/user_update/<string:email>/', methods=['PATCH'])
def user_update(email):
    error = None
    actions = []
    data = {}

    try:
        data = UserSchema().load(request.json)
    except ValidationError as err:
        error = err

    for key, value in data.items():
        actions.append(getattr(UserModel, key).set(value))
    user = UserModel.get(email)
    user.update(actions=actions)

    return {
        "status": "error" if error else "success",
        "error": error,
        "data": UserSchema().dump(user)
    }


@user_blueprint.route('/user_delete/<string:email>/', methods=["DELETE"])
def user_delete(email):
    user = UserModel.get(email)
    user.delete()
    return {
        "status": "success",
        "message": "User deleted successfully!"
    }
