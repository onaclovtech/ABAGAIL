
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
     def __init__ (self, data = None, label = None, weight = None, ds = None, val = None, i = None, o = None):
        if data:
            self.data = data # Vector
        if label:
            self.label = label # Instance
        if ds:
            self.data = DenseVector(ds)
        if val:
            self.data = DenseVector(size = 1)
            self.data.set(0, val)
        # if i:
            # self.data = DenseVector(1)
            # self.data.set(0, val)
        # if o:
            # self.label = Instance(o)
        if weight:
            self.weight = weight # double
        else:
            self.weight = 1.0
    
#    public Instance(int i, int o) {
#        this(i); # 
#        label = new Instance(o);
#    public Instance(double[] ds, int i) {
#        this(ds);
#        label = new Instance(i);
#    public Instance(double[] ds, boolean b) {
#        this(ds);
##        label = new Instance(b);
#    public Instance(boolean val) {
#        this(val ? 1 : 0);

    
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
        return self.data.get(i)
    
    
#/**
#* Get the ith discrete value
#* @param i the value to get
#* @return the value
#*/
     def getDiscrete(self, i=0):
        #return Math.round(data.get(i))
         print "" # This needs to be fixed
         
    

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
        return Instance(val = self.label)
    
#/**
#* Get the data vector
#* @return the data
#*/
     def getData(self):
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
        self.data = vector
    

#/**
#* Set the label for self instance
#* @param instance the label
#*/
     def setLabel(self, instance):
        self.label = instance
    

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
        print self
        if 'label' in self.__dict__:
            return Instance(data = self.data.copy(), label = self.label.copy(), weight = self.weight)
        else:
            return Instance(data = self.data.copy(), weight = self.weight)
        
    
    
#/**
#* @see java.lang.Object#toString()
#*/
     def toString():
        result = data.toString()
        if (label != null):
            result += " : " + label.toString()
        
        if (weight != 1.0):
            result += " x " + weight
        
        return result
    



