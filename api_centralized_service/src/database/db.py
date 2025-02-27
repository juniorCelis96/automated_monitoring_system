import psycopg2
from psycopg2 import DatabaseError
from decouple import config


def get_connection():
    try:
        return psycopg2.connect(
            host = config('DATABASE_HOST'),
            user = config('DATABASE_USER'),
            port = config('DATABASE_PORT'),
            password = config('DATABASE_PASSWORD'),
            database = config('DATABASE_NAME')
        )
    except DatabaseError as e:
        raise Exception("Error al intentar conectar a la base de datos: ", e)