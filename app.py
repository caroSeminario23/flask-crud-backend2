from flask import Flask, Blueprint
from utils.db import db #importar esa instancia
from services.predio import predios
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

app = Flask(__name__)
#predio = Blueprint('predio', __name__) # Permite crear una instancia personalizada
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

#SQLAlchemy(app)
db.init_app(app)
app.register_blueprint(predios) # Permite registrar la instancia personalizada

with app.app_context():
    db.create_all() #se va a ejecutar en caso la clase contact no existiera

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)