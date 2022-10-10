from os import environ as env


# automatically updates some dev envs. 
try:
    __import__('envs.py')
except ImportError:
    pass

# Flask config
IP = env.get('IP', '0.0.0.0')
PORT = env.get('PORT', 8080)
SERVER_NAME = env.get('SERVER_NAME', 'devcade.csh.rit.edu')
PREFERRED_URL_SCHEME = env.get('PREFERRED_URL_SCHEME', 'https')

SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI', "Probably-some-postgres-bs")
SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
# OpenID Connect SSO config CSH
OIDC_ISSUER = env.get('OIDC_ISSUER', 'https://sso.csh.rit.edu/auth/realms/csh')
OIDC_CLIENT_ID = env.get('OIDC_CLIENT_ID', 'devcade')
OIDC_CLIENT_SECRET = env.get('OIDC_CLIENT_SECRET', 'NOT-A-SECRET')