from orator import DatabaseManager
from orator import Model
from orator.orm import has_many,belongs_to

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


class Label(Model):
    __fillable__ = ['name','type','sample_id']

    @belongs_to
    def sample(self):
        return Sample



class Sample(Model):
    __fillable__ = ['name']

    @has_many
    def labels(self):
        return Label





