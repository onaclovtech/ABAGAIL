
from src.util.linalg.DenseVector import *

#/**
#* The abstract class representing some instance.
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class Instance:

#/**
#* The label for self instance
#*/
    #Instance label
    
#/**
#* The vector storing the data
#*/
    #Vector data
    
#/**
#* The weight of the instance
#*/
    #double weight
#/**
#* Make a instance from the given data
#* @param data the data itself
#* @param label the label
#* @param weight the weight
#* @param dataSet the data set
#*/
     # double weight
     # Instance label
     # Vector data 
     # Vector v
     # double[] ds
     # double, int val
     # int o
     # int i
     # double ds
     # boolean b
     def __init__ (self, data = None, label = None, weight = None, ds = None, val = None, i = None, o = None, b = None):
        #print "Instance.__init__.Parameters: " + "data: " + str(data) + " label: " + str(label) + " weight: " + str(weight) + " ds: " + str(ds) + " val: " + str(val) 
        if not data is None:
            if not isinstance(data, Vector):
                raise TypeError('Vector Class Required: ' + str(data.__class__))
            self.data = data # Vector
        if not label is None:
            if not isinstance(label, Instance):
                raise TypeError ('Instance Required for all Labels: ' + str(label.__class__))
            self.label = label # Instance
        if not ds is None:
            if not isinstance(ds, list):
                raise TypeError('Array of "doubles" required here: '  + str(ds.__class__))
            self.data = DenseVector(data = ds)
        if not val is None:
            if not isinstance(val, (int, long, float, complex)):
                raise TypeError('Expected a number here ' + str(val.__class__))
            self.data = DenseVector(size = 1)
            self.data.set(0, val)
        if not i is None:
            this(val = i)
        if not o is None:
            self.label = Instance(val = float(o))
        if not b is None:
            if b:
                self.label = Instance(val = 1.0)
            else:
                self.label = Instance(val = 0.0)
        if not weight is None:
            self.weight = weight # double
        else:
            self.weight = 1.0
        
        if data is None and ds is None and val is None:
          print val
          print ','.join([str(data), str(label), str(weight), str(ds), str(val), str(i), str(o), str(b)])
          raise TypeError('WHAT IS HAppening?')
          

    
#/**
#* Get the size of the instance
#* @return the size
#*/
     def size(self):
        return self.data.size()
    
#/**
#* Get the ith continuous value
#* @param i the value to get
#* @return the value
#*/
     def getContinuous(self, i=0):
        #print "instance.getContinuous.data.get" + str(type(self.data.get(i)))
        if isinstance(self.data.get(i), Instance):
            raise TypeError('I dont even')
        
        return self.data.get(i)
    
    
#/**
#* Get the ith discrete value
#* @param i the value to get
#* @return the value
#*/
     def getDiscrete(self, i=0):
        #print "instance.getDiscrete " + str(self.__dict__)
        return int(round(self.data.get(i)))
       #  raise StubError('getDiscrete Not Implemented Yet')
         
    

#/**
#* Get a plus or minus value
#* @return a plus or minus boolean value
#*/
     def getPlusMinus(self):
        if (self.getDiscrete() == 1):
            return 1
        else:
            return -1
    
    
#/**
#* Get the boolean value
#* @return the boolen value
#*/
     def getBoolean(self):
        return self.getDiscrete() == 1
    
    
#/**
#* Get the label for self instance
#* @return the label
#*/
     def getLabel(self):
        #print "instance.getLabel: " + str(type(self.label))
        return self.label
    
#/**
#* Get the data vector
#* @return the data
#*/
     def getData(self):
        #print "instance.self.getData().self.data" + str(self.data.__class__)
        return self.data
    

#/**
#* Get the weight of self instance
#* @return the weight
#*/
     def getWeight(self):
        return self.weight
    

#/**
#* Set the data vector
#* @param vector the data vector
#*/
     def setData(self, vector):
        #print "instance.setData.vector" + str(vector)
        self.data = vector
    

#/**
#* Set the label for self instance
#* @param instance the label
#*/
     def setLabel(self, instance):
        if not isinstance(instance, Instance):
            raise TypeError('Instance Required ' + str(instance.__class__))
        self.label = instance
        #print "instance.self" + str(self.__dict__)
    

#/**
#* Set the weight for the instance
#* @param d the weight
#*/
     def setWeight(self, d):
        self.weight = d
    
    
#/**
#* Make a instance
#* @return the copy
#*/
     def copy(self):
        #print 'instance.copy' + str(self)
        if 'label' in self.__dict__:
            #print "instance.setData.vector" + str(vector)
            return Instance(data = self.data.copy(), label = self.label.copy(), weight = self.weight)
        else:
            return Instance(data = self.data.copy(), weight = self.weight)
        
    
    
#/**
#* @see java.lang.Object#toString()
#*/
     def toString(self):
        #print self.data.__class__
        
        result = self.data.toString()
        #print 'instance.tostring.self.__dict__' + str(self.__dict__)
        if 'label' in self.__dict__.keys():
            result += " : " + self.label.toString()
        if (self.weight != 1.0):
            result += " x " + self.weight
        
        return result
    



