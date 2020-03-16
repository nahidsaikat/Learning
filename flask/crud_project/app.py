from flask import Flask, request
from marshmallow import ValidationError

from models.users import UserModel
from schemas.users import UserSchema

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/user_list/')
def user_list():
    return {"user_list": UserSchema(many=True).dump(UserModel.scan())}


@app.route('/user_create/', methods=['POST'])
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


@app.route('/user_update/<string:email>/', methods=['PATCH'])
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


@app.route('/user_delete/<string:email>/', methods=["DELETE"])
def user_delete(email):
    user = UserModel.get(email)
    user.delete()
    return {
        "status": "success",
        "message": "User deleted successfully!"
    }


# user = UserModel('test@domain.com', first_name='Nahid', last_name='Saikat')
# user.save()

if not UserModel.exists():
    UserModel.create_table(wait=True)

if __name__ == '__main__':
    app.run()
