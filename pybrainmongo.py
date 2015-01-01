import pymongo
from bson.code import Code
from pybrain.structure import LinearLayer, SigmoidLayer, RecurrentNetwork, FeedForwardNetwork
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet, ClassificationDataSet
from pybrain.structure.connections.shared import MotherConnection
from datetime import datetime

#Make base marking(categorization) like in iris dataset

'''Examples http://habrahabr.ru/post/134590/ '''

'''Construct neural network with PyBrain and MongoDB'''

#Mongo Layer for getting better parameters from mongo
class MongoLayer:
    def __init__(self, value, name, items):
        self.value = value
        self.name = name
        self.items = items

#DataSet provide in mongo
class MongoInputLayer(MongoLayer):
    def __init__(self, value, name):
        MongoLayer.__init__(value, name)

class MongoOutputLayer(MongoLayer):
   def __init__(self, value, name):
        MongoLayer.__init__(value, name) 




#http://pybrain.org/docs/tutorial/netmodcon.html
'''collection - mongoBase'''
class BrainMongo:
    def __init__(self, neuralModel, collection):
        self.collection = collection
        self.model = neuralModel
    def insert(self, data):
        self.collection.insert(data)

    #Getting function of activation
    def activate(self, activateName):
        result = self.collection.find_one({"name":activateName})
        return result["activate"]

    def addDataSet(self,dataset):
        pass

    #{Input, Hidden, Output}. layer
    def addLayers(self, inputs, outputs, hidden):
        if isinstance(self.model, RecurrentNetwork):
            self.model.addInputModule(LinearLayer(inputs, name='input'))
            self.model.addModule(SigmoidLayer(hidden, name='hidden'))
            self.model.addOutputModel(LinearLayer(output, name='output'))
            addRecurrentConnection(FullConnection(n['hidden'], n['hidden'], name='c3'))
            self.model.sortModules()
            self.model.activate([1.1,2.2])

    def addLayers2(self, inputs, outputs, hidden):
       if isinstance(self, model, FeedForwardNetwork):
            self.model.addInputModule(inputs)
            self.model.addModel(hidden)
            self.model.addOutputModel(outputs)


    #RNN or FFN
    def addModel(self, neuralType):
        self.model = neuralType

    def addSample(self, samples):
        raise NotImplementedError

    def SaveNetwork(self, network):
        raise NotImplementedError

    def insertvalue(self, key, value):
        return self.collection.insert({key:value, "C":"D"})

    def insertwithResult(self, key, result, value):
        output = self.collection.find_one(result)
        #Build network and insert results

    def remove(self, key):
        self.collection.remove(key)

    #Classify data and after- insert(or not) to mongo
    def classify(self, isinsert):
        if isinsert:
            self.insert({'page1':'Value'})

''' Things which can be loaded from MongoDB
typeset:[ Classification, Reinforcment, Importance,
        Sequence, Supervised, Unsupervised]
'''
'''All i/o operations from here'''
class MongoProvide:
    def __init__(self, collection,*args, **kwargs):
        self.collection = collection
    def dataSet(self, typeset, name):
        class InnerDataSet:
            @staticmethod
            def load(**kwargs):
                dbname = kwargs.get('name')
                return self.collection[name]
                #print(self.collection)
                #return self.collection.find_one({"type":'dataset',"name": name})

            @staticmethod
            def save(name, **kwargs):
                dims = kwargs.get('dimension',2)
                classes = kwargs.get('nb_classes')
                typeset = kwargs.get('typeset')
                class_labels = kwargs.get('class_label')
                outputArgs = GenerateOutputParams()
                outputArgs.addFiled('typename', typeset)
                '''insertion = {
                    "typename": typeset,
                    "dimension":dims,
                    "nb_classes":classes,
                    "data":now()
                    "class_labels":class_labels
                }'''
                self.collection.insert(outputArgs.output())

        return InnerDataSet

    def classifer(labels, data):
        """ data in format (value, label)
        """
        clsff = ClassificationDataSet(2,class_labels=labels)
        for d in data:
            clsff.appendLinked(d[0], d[1])
        clsff.calculateStatistics()



class GenerateOutputParams:
    def __init__(self):
        self.outputfields={}

    def addFiled(self, name, value,**kwargs):
        if name not in self.outputfields:
            self.outputfields[name] = value

    def output(self):
        return self.outputfields


class DataSets:
    def __init__(self, mongo):
        self.mongo = mongo

    """ Return all possible datasets """
    def find(self):
        return self.mongo.find({'typedataset'})

class Network(object):
    """docstring for Network"""
    def __init__(self, *args,**kwargs):
        super(Network, self).__init__()
        self.network = buildNetwork(
            kwargs.get('input'),
            kwargs.get('hidden'),
            kwargs.get('output')
            )

        ClassificationDataSet(2, nb_classes=2, class_labels= kwargs.get('labels'))
        self.active = kwargs.get('activate')
        self.network.activate(self.active)


'''DS = ClassificationDataSet(2, nb_classes=2, class_labels=['Fish','Chips'])
ll = LinearLayer(2, name='foo')
DS.appendLinked([ 0.1, 0.5 ]   , [0])
DS.appendLinked([ 1.2, 1.2 ]   , [1])
DS.appendLinked([ 1.4, 1.6 ]   , [1])
DS.appendLinked([ 1.6, 1.8 ]   , [1])
DS.appendLinked([ 1.8, 2.0 ]   , [1])
DS.appendLinked([ 0.10, 0.80 ] , [2])
DS.appendLinked([ 0.20, 0.90 ] , [2])
print(DS.calculateStatistics())
print DS.classHist
print DS.getClass(1)'''

client = pymongo.MongoClient('localhost', 27017)
b = BrainMongo(client, ClassificationDataSet)
dataset = MongoProvide(client).dataSet('typeSet', 'test').load()
b.addDataSet(dataset)

