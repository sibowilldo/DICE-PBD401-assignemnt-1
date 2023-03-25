import os

app_config = {'SECRET_KEY': os.getenv('SECRET_KEY', os.urandom(32)),
              'DEBUG': os.getenv('FLASK_DEBUG', True),
              'DB_CONNECTION': os.getenv('DB_CONNECTION', ''),
              'DB_USERNAME': os.getenv('DB_USERNAME', ''),
              'DB_PASSWORD': os.getenv('DB_PASSWORD', ''),
              'DB_HOST': os.getenv('DB_HOST', ''),
              'DB_PORT': os.getenv('DB_PORT', ''),
              'DB_DATABASE': os.getenv('DB_DATABASE', ''),
              'SQLALCHEMY_TRACK_MODIFICATIONS': os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False),
              'WTF_CSRF_SECRET_KEY': os.getenv('WTF_CSRF_SECRET_KEY', os.urandom(32)),
              'API_URL': os.getenv('API_URL', '/api/v1'),
              'AUTH0_DOMAIN': os.getenv('AUTH0_DOMAIN', ''),
              'AUTH0_CLIENT_ID': os.getenv('AUTH0_CLIENT_ID', ''),
              'AUTH0_API_AUDIENCE': os.getenv('AUTH0_API_AUDIENCE', ''),
              }

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
