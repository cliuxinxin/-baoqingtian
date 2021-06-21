
from datetime import datetime
from pony.orm import *


db = Database(
    {   'provider':'sqlite',
        'filename':'pony.db', 
        'create_db':True})


class Resource(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    dt = Optional(datetime)
    tags = Set('Tag')
    processes = Set('Process')


class Tag(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    dt = Optional(datetime)
    resources = Set(Resource)
    models = Set('Model')


class Process(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    dt = Optional(datetime)
    resources = Set(Resource)
    item = Required('Item')


class Item(db.Entity):
    id = PrimaryKey(int, auto=True)
    idx = Optional(str)
    process = Optional(Process)
    dt = Optional(datetime)
    labels = Set('Label')
    batches = Set('Batch')
    tests = Set('Test')


class Label(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    dt = Optional(datetime)
    item = Required(Item)
    train = Optional('Train')


class Batch(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    dt = Optional(datetime)
    items = Set(Item)


class Model(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    dt = Optional(str)
    tags = Set(Tag)
    train = Optional('Train')


class Train(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    dt = Optional(str)
    model = Required(Model)
    result = Optional(str)
    parameters = Optional(str)
    label = Required(Label)
    evaluations = Set('Evaluation')


class Test(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    items = Set(Item)
    evaluations = Set('Evaluation')


class Evaluation(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    dt = Optional(str)
    test = Required(Test)
    train = Required(Train)
    result = Optional(str)



db.generate_mapping()