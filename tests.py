import brainmongo
from pybrain.datasets import ClassificationDataSet
import unittest
from pymongo import MongoClient


client = MongoClient()
db = client.mlbase
db = client["mlbase"]
collection =db.mlbase
class TestStart(unittest.TestCase):
    """docstring for TestStart"""
    def test_load(self):
        b = brainmongo.BrainMongo(collection)
        net = brainmongo.buildNetwork(2,4,1)
        net.activate(b.activate())
        print(b.activate())

    def test_write_dataset(self):
        b = brainmongo.MongoProvide(collection).\
        dataSet(ClassificationDataSet,)
        b.save('neurodb', 'dimention' = 3)


    '''def test_load_dataset(self):
        b = brainmongo.MongoProvide(collection).dataSet(ClassificationDataSet,'a')
        b.load(name="ClassificationDataSet")'''




unittest.main()
