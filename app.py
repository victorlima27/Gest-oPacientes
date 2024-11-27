from flask import Flask, jsonify
from flask.cli import AppGroup
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flasgger import Swagger
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)
swagger = Swagger(app)
migrate = Migrate(app,db)
seed_cli = AppGroup('seed')

# Importando as rotas
from rotas import *
# Importando Seed
from seed import *
# Importando os modelos
from models import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
