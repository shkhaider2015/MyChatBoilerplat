from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from myApp.config import Config
from flask_login import LoginManager
from flask_bcrypt import Bcrypt 
from flask_migrate import Migrate
from flask_mail import Mail
from myApp.database import init_db
from flask_cors import CORS
from flask_socketio import SocketIO



db = SQLAlchemy()
migrate = Migrate()
# bcrypt = Bcrypt()
# login_manager = LoginManager()
# login_manager.login_view = 'users.login'
# mail = Mail()
cors = CORS()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    socketio = SocketIO(app)

    db.init_app(app)
    cors.init_app(app)


    
    # Create Database
    init_db()
    migrate.init_app(app, db)

    socketio = SocketIO(app)

    # from myApp.User.routes import user_blueprint
    # from myApp.Client.routes import clients
    # from myApp.Meetings.routes import meetings
    # from myApp.Projects.routes import projects

    
    # app.register_blueprint(user_blueprint)
    # app.register_blueprint(clients)
    # app.register_blueprint(meetings)
    # app.register_blueprint(projects)

    return socketio