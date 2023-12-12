from os import environ as env

# automatically updates some dev envs. 
try:
    __import__('envs.py')
except ImportError:
    pass

# Flask config
SERVER_NAME = env.get('SERVER_NAME', 'localhost:5000')
PREFERRED_URL_SCHEME = env.get('PREFERRED_URL_SCHEME', 'https')

POSTGRESQL_USER = env.get('POSTGRESQL_USER', '')
POSTGRESQL_PASSWORD = env.get('POSTGRESQL_PASSWORD')
POSTGRESQL_DATABASE = env.get('POSTGRESQL_DATABASE', 'usersDB')
POSTGRESQL_IP = env.get('POSTGRESQL_IP')
SQLALCHEMY_DATABASE_URI = env.get(
    'SQLALCHEMY_DATABASE_URI', "postgresql://" + str(POSTGRESQL_USER) + ":" + str(POSTGRESQL_PASSWORD) + "@" + str(POSTGRESQL_IP) + "/" + str(POSTGRESQL_DATABASE) + "")
if POSTGRESQL_USER == '':
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = 'False'

# OpenID Connect SSO config CSH
OIDC_ISSUER = env.get('OIDC_ISSUER', 'https://sso.csh.rit.edu/auth/realms/csh')
OIDC_CLIENT_ID = env.get('OIDC_CLIENT_ID', 'devcade')
OIDC_CLIENT_SECRET = env.get('OIDC_CLIENT_SECRET', 'NOT-A-SECRET')

GOOGLE_OIDC_ISSUER = env.get('GOOGLE_OIDC_ISSUER', 'https://sso.csh.rit.edu/auth/realms/csh')
GOOGLE_OIDC_CLIENT_ID = env.get('GOOGLE_OIDC_CLIENT_ID', 'devcade')
GOOGLE_OIDC_CLIENT_SECRET = env.get('GOOGLE_OIDC_CLIENT_SECRET', 'NOT-A-SECRET')

DEVCADE_API_URI = env.get('DEVCADE_API_URI')
FRONTEND_API_KEY = env.get('FRONTEND_API_KEY')

DEVCADE_IS_DEV = env.get('DEVCADE_IS_DEV')

SECRET_KEY = env.get('SECRET_KEY') or os.urandom(16)
