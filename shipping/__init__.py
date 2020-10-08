from shipping.config import Config
from flask import Flask
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(db, app)

    from shipping.main.views import main
    from shipping.users.views import users
    from shipping.clients.views import clients
    from shipping.receivers.views import receivers
    from shipping.packages.views import packages
    from shipping.report.views import report

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(clients)
    app.register_blueprint(receivers)
    app.register_blueprint(packages)
    app.register_blueprint(report)

    return app


