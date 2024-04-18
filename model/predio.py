from utils.db import db # Importamos la instancia de la clase SQLAlchemy
from dataclasses import dataclass 

# EN RESTAURACION
@dataclass # Indica que la clase debe ser tratada con esa librería
class Predio(db.Model):
    # Vincula la clase Predio con la tabla predio de la base de datos, para lograr la persistencia

    id_predio: int
    id_tipo_predio: int
    description: str
    ruc: str
    telefono: str
    correo: str
    direccion: str
    idubigeo: str
    id_persona: int
    url_imagen: str
    total_mdu: int

    id_predio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_tipo_predio = db.Column(db.Integer)
    description = db.Column(db.String(80))
    ruc = db.Column(db.String(20))
    telefono = db.Column(db.String(12))
    correo = db.Column(db.String(80))
    direccion = db.Column(db.String(100))
    idubigeo = db.Column(db.String(6))
    id_persona = db.Column(db.Integer)
    url_imagen = db.Column(db.String(120))
    total_mdu = db.Column(db.Integer)

    def __init__(self, id_tipo_predio, description, ruc, telefono, correo, direccion,
                 idubigeo, id_persona, url_imagen, total_mdu):
        
        self.id_tipo_predio = id_tipo_predio
        self.description = description
        self.ruc = ruc
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.idubigeo = idubigeo
        self.id_persona = id_persona
        self.url_imagen = url_imagen
        self.total_mdu = total_mdu