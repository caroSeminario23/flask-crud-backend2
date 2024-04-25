from dotenv import load_dotenv
import os

load_dotenv() # Se crea la instancia de la clase y lee las variables de entorno de env

# Descarga de las variables de entorno
user = os.environ['USER']
pwd = os.environ['PASSWORD']
host = os.environ['HOST']
database = os.environ['DATABASE']
server = os.environ['SERVER']

DATABASE_CONNECTION = f'{server}://{user}:{pwd}@{host}/{database}'