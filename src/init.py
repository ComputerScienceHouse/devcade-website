import os
import pytz
import flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_pyoidc.flask_pyoidc import OIDCAuthentication
from flask_pyoidc.provider_configuration import ProviderConfiguration, ClientMetadata


app = flask.Flask(__name__)
app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))

# time setup for the server side time
eastern = pytz.timezone('America/New_York')

# OIDC Authentication
CSH_AUTH = ProviderConfiguration(issuer=app.config["OIDC_ISSUER"],
                                 client_metadata=ClientMetadata(
                                     app.config["OIDC_CLIENT_ID"],
                                     app.config["OIDC_CLIENT_SECRET"]))
auth = OIDCAuthentication({'default': CSH_AUTH},
                          app)

auth.init_app(app)
app.secret_key = os.urandom(16)

# DB
db = SQLAlchemy(app)
migrate = Migrate(app, db)