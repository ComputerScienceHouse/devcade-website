from os import environ as env

# automatically updates some dev envs. 
try:
    __import__('envs.py')
except ImportError:
    pass

# Flask config
IP = env.get('IP', '0.0.0.0')
PORT = env.get('PORT', 8080)
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

AWS_ACCESS_KEY_ID = env.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = env.get('AWS_SECRET_ACCESS_KEY', '')

# OpenID Connect SSO config CSH
OIDC_ISSUER = env.get('OIDC_ISSUER', 'https://sso.csh.rit.edu/auth/realms/csh')
OIDC_CLIENT_ID = env.get('OIDC_CLIENT_ID', 'devcade')
OIDC_CLIENT_SECRET = env.get('OIDC_CLIENT_SECRET', 'NOT-A-SECRET')

DEVCADE_API_URI = env.get('DEVCADE_API_URI')