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
        assert len(list(resources)) == 1
        assert resources[0].name == 'data/resources/PeopleDaily199801.txt'