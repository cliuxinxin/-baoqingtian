import configparser
import glob
import json
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

    def read_resource(self,resource):
        texts = []
        with open(resource,encoding="utf-8") as f:
            for line in f:
                json_f = json.loads(line)
                texts.append(json_f)
        return texts


    def process_texts(self,texts):
        for entry in texts:
            sentence = entry['text']
            label = []
            for key1,value1 in entry['label'].items():
                for key2,value2 in value1.items():
                    value2[0].append(key1)
                    label.append(value2[0])
            self.save_sentence_label(sentence,label)

    def save_sentence_label(self,sentence,label):
        label = repr(label)
        sample = Sample.first_or_create(name=sentence)
        Label.first_or_create(name=label,type='ground_true',sample_id=sample.id)

    def gernerate_batch(self):
        batch = Batch.first_or_create(name='test_random')
        samples = Sample.limit(10).get()
        for sample in samples:
            batch.samples().attach(sample.id)

data = Data()
data.gernerate_batch()

