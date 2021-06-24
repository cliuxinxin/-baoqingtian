from orator import DatabaseManager
from orator import Model

config = {
    'mysql': {
        'driver': 'sqlite',
        'database': 'baoqingtian.db',
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)



class Resource(Model):
    __fillable__ = ['name']



