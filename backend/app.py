import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import CSRFProtect
from dotenv import load_dotenv
from flask_login import LoginManager

load_dotenv('.env')

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    with app.app_context():
        app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

        database_path = f'{os.getenv("DB_CONNECTION", "")}://{os.getenv("DB_USERNAME")}:' \
                        f'{os.getenv("DB_PASSWORD", "")}@{os.getenv("DB_HOST")}:' \
                        f'{os.getenv("DB_PORT")}/{os.getenv("DB_DATABASE")}'

        app.config["SQLALCHEMY_DATABASE_URI"] = database_path
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        csrf = CSRFProtect(app)

        db.init_app(app)

        login_manager = LoginManager()
        login_manager.login_view = 'auth.login'
        login_manager.init_app(app)

        from database import models

        @login_manager.user_loader

        def load_user(user_id):
            return models.User.query.get(int(user_id))

        from auth import auth as auth_blueprint

        app.register_blueprint(auth_blueprint)

        # blueprint for non-auth parts of app
        from routes import main as main_blueprint

        app.register_blueprint(main_blueprint)

        return app
