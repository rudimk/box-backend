import os
from orator import DatabaseManager

config = {
    'mysql': {
        'driver': 'mysql',
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWD')
    }
}

db = DatabaseManager(config)