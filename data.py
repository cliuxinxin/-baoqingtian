import configparser
import glob

class Data():
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read('config.ini')
        pass

    def list_resources(self):
        res_document = 'data/' + self.conf['config']['resources'] + '/*' 
        resources = glob.glob(res_document)
        return resources

data = Data()



