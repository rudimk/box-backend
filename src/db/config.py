import os
from orator import DatabaseManager, Schema

DATABASES = {
    'mysql': {
        'driver': 'mysql',
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWD')
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)