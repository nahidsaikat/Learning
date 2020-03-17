from flask import Flask

from models.users import UserModel
from views.users import user_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint)

if not UserModel.exists():
    UserModel.create_table(wait=True)

if __name__ == '__main__':
    app.run()
