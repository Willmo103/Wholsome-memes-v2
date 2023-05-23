from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from .utils import init_db_config, init_uploads_folder, init_secret_key
import dotenv, os
# from flask_migrate import Migrate

# set the project root directory as an environment variable to be used in other modules
os.environ["PROJECT_ROOT"] = os.path.abspath(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)
)
os.environ["ENV_PATH"] = os.path.join(os.environ.get("PROJECT_ROOT"), ".env")
check_for_dotenv = os.path.exists(os.environ.get("ENV_PATH"))
print(f".env file exists: {check_for_dotenv}")

if check_for_dotenv:
    # if the .env file exists, load it into the environment
    dotenv.load_dotenv(dotenv_path=os.environ.get("ENV_PATH"))
else:
    print("No .env file found. Attempting to load environment variables from OS.")


# initialize the app configuration with the utils module and Config class
class Config:
    host_name = os.environ.get("HOST_NAME")
    port = os.environ.get("PORT")
    database_name = os.environ.get("DATABASE_NAME")
    database_username = os.environ.get("DATABASE_USERNAME")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{database_username}@{host_name}:{port}/{database_name}"
    )
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO")
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_ID = os.environ.get("CLIENT_SECRET")
    USER_AGENT = os.environ.get("USER_AGENT")
    ADMIN_SECRET = os.environ.get("ADMIN_SECRET")



# create an instance of the Config class
conf = Config()

# initialize the database
db:SQLAlchemy = SQLAlchemy()

# initialize the login manager
login_manager = LoginManager()

# set the login view for the login manager
login_manager.login_view = "routes.login"

# create the app factory function and register the blueprints and database
def create_app():
    # create the flask app instance
    app = Flask(__name__)

    # load the app configuration
    app.config.from_object(Config)

    # initialize the database
    db.init_app(app)

    # initialize the login manager
    login_manager.init_app(app)

    # using the app context, register the blueprints and models
    with app.app_context():

        # import the routes and models modules
        from . import routes
        from . import models

        # register the blueprints
        # app.register_blueprint(routes.endpoint)

        # create the database tables if they do not exist
        # db.create_all()

        # return the app instance
        return app


# create the app instance
app = create_app()
