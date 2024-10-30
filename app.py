from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_mail import Mail

app = Flask(__name__)

# # Email da Quantum # #
# app.config['MAIL_SERVER'] = 'X.X.X.X'  # Use o servidor de e-mail apropriado
# app.config['MAIL_PORT'] = 587  # Use a porta correta para envio de e-mails
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'nome.sobrenome@dominio'
# app.config['MAIL_PASSWORD'] = ''
### app.config['MAIL_DEFAULT_SENDER'] = 'nome.sobrenome@dominio'  # Defina o remetente aqui

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

# Importe suas rotas


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4569, debug=True)
