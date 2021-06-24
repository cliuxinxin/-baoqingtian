import configparser
import glob
from orms import *

class Data():
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read('config.ini')
        pass

    def list_resources(self):
        res_document = 'data/' + self.conf['config']['resources'] + '/*' 
        resources = glob.glob(res_document)
        return resources

    def update_resources(self):
        resources = self.list_resources()
        for resource in resources:
            Resource.first_or_create(name=resource) 

    def view_resources(self):
        return Resource.all()




