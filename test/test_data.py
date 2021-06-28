import unittest
from data import Data

class TestData(unittest.TestCase):

    def test_data_list_resouces(self):
        data = Data()
        resources = data.list_resources()
        assert resources[0] == 'data/resources/PeopleDaily199801.txt'

    def test_data_update_resource(self):
        data = Data()
        data.update_resources()
        resources = data.view_resources()
        assert len(list(resources)) == 2
        assert resources[0].name == 'data/resources/PeopleDaily199801.txt'

    def test_data_read_resource(self):
        data = Data()
        resources = data.view_resources()
        resource = resources[1].name
        read_data = data.read_resource(resource) 
        assert len(read_data) == 12091