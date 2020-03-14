from flask import Flask, request

from models.users import UserModel

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/user_list/')
def user_list():
    all_users = []
    for item in UserModel.scan():
        all_users.append(item.__dict__['attribute_values'])
    return {"user_list": all_users}


@app.route('/user_create/', methods=['POST'])
def user_create():
    user = UserModel(**request.json)
    user.save()
    return {
        "status": "success",
        "message": "User created successfully!",
        "email": user.email,
        "data": user.__dict__['attribute_values']
    }


@app.route('/user_update/<string:email>/', methods=['PATCH'])
def user_update(email):
    actions = []
    for key, value in request.json.items():
        actions.append(
            getattr(UserModel, key).set(value)
        )
    user = UserModel.get(email)
    user.update(
        actions=actions
    )
    return {
        "status": "success",
        "message": "User updated successfully!",
        "email": user.email,
        "data": user.__dict__['attribute_values']
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
