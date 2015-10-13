from src.shared.AttributeType import *
from src.util.linalg.Vector import *

#/**
#* A data set description contains information
#* about the attributes of a data set
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class DataSetDescription:
    
#/**
#* The description of the label type
#*/
#    DataSetDescription labelDescription
    
#/**
#* The types of the attributes
#*/
#    AttributeType[] types
    
#/**
#* The maximum value
#*/
#    Vector max
    
#/**
#* The minimum value instance
#*/
#    Vector min
    
#/**
#* Make a new data set description
#* @param types the types of the data
#* @param min the minimum value
#* @param max the maximum value
#* @param labelDescription the description of the label
#*/
     def __init__(self, types = None, min  = None, max  = None, labelDescription = None, dataSet = None):
        if not types is None:
            if not isinstance(types, list):
                raise TypeError("Expected list got " + str(types.__class__))
            self.types = types
        if not min is None:
            if not isinstance(min, Vector):
                raise TypeError("Expected Vector got " + str(types.__class__))
            self.min = min
        if not max is None:
            if not isinstance(max, Vector):
                raise TypeError("Expected Vector got " + str(types.__class__))      
            self.max = max
            if min is None:
                min = DenseVector(size = max.size())
        if not labelDescription is None:
            if not isinstance(labelDescription, DataSetDescription):
                raise TypeError("Expected Vector got " + str(types.__class__))                   
            self.labelDescription = labelDescription 
        if not dataSet is None:
            induceFrom(dataSet)


    
#/**
#* Get the discrete max
#* @param i the attribute index
#* @return the max of the attribute
#*/
     def getDiscreteRange(self, i = 0):
        return int(self.max.get(i) + 1)
    
    

#/**
#* Get the continuous range
#* @param i the attribute index
#* @return the range of the attribute
#*/
     def getRange(self, i = 0):
        return self.getMax(i) - self.getMin(i)
    
    
    
#/**
#* Get the continuous max
#* @param i the attribute index
#* @return the max of the attribute
#*/
     def getMax(self, i = 0):
        return self.max.get(i)
    

#/**
#* Get the continuous max
#* @param i the attribute index
#* @return the max of the attribute
#*/
     def getMin(self, i = 0):
        return self.min.get(i)

#/**
#* Get the description of the label
#* @return the description of the label
#*/
     def getLabelDescription(self):
        return self.labelDescription

#/**
#* Get the maximum value
#* @return the maximum value
#*/
     def getMaxVector(self):
        return self.max

#/**
#* Get the types of the data
#* @return the types
#*/
     def getAttributeTypes(self):
        return self.types
    
#/**
#* Get the attribute count
#* @return the count
#*/
     def getAttributeCount(self):
        return len(self.types)
    

#/**
#* Get the min of the data
#* @return the min
#*/
     def getMinVector(self):
        return self.min

#/**
#* Set the label description
#* @param description the new description
#*/
     def setLabelDescription(self, description):
        if not isinstance(description, DataSetDescription):
            raise TypeError('Expected DatasetDescription got ' + str(description.__class__))
        self.labelDescription = description

#/**
#* Set the max
#* @param instance the new max
#*/
     def setMaxVector(self, instance):
        if not isinstance(instance, Vector):
            raise TypeError("Expected Vector got " + str(instance.__class__))
        self.max = instance
    

#/**
#* Set the min
#* @param instance the new min
#*/
     def setMinVector(self, instance):
        if not isinstance(instance, Vector):
            raise TypeError("Expected Vector got " + str(instance.__class__))
        self.min = instance
    

#/**
#* Set the types
#* @param types the new types
#*/
     def setAttributeTypes(self, types):
        if not isinstance(types, list):
            raise TypeError("Expected Vector got " + str(types.__class__))
        self.types = types
    
#/**
#* Induce from the given data set
#* @param data the data set
#*/
     def induceFrom(self, data):
        if not isinstance(data, DataSet):
            raise TypeError("Expected DataSet got " + str(data.__class__))
        hasLabels = False
        i = 0
        while (data.get(i) is None):
            i = i + 1
        if (i >= data.size()):
            return
        
        if (self.max is None):
            self.max = data.get(i).getData().copy()
        
        if (self.min is None):
            self.min = data.get(i).getData().copy()
        
        if (self.types is None):
            self.types = [AttributeType.BINARY] * data.get(i).size() # Should fill up an array of the size with AttributeTypes(0)
        
        for k in range(i, data.size()):
            cur = data.get(k)
            if (cur is None):
                continue
            hasLabels = hasLabels or (not cur.getLabel() is None)
            self.max.maxEquals(cur.getData())
            self.min.minEquals(cur.getData())
            for j in range(len(self.types)):
                if ((self.types[j] == AttributeType.BINARY) and (cur.getContinuous(j) != 1) and (cur.getContinuous(j) != 0)):
                    self.types[j] = AttributeType.DISCRETE
                
                if ((self.types[j] == AttributeType.DISCRETE) and (cur.getDiscrete(j) != cur.getContinuous(j))):
                    self.types[j] = AttributeType.CONTINUOUS      

        if (hasLabels):
            if (self.labelDescription is None):
                self.labelDescription = DataSetDescription()
            
            self.labelDescription.induceFrom(data.getLabelDataSet())

#/**
#* @see java.lang.Object#toString()
#*/
     def toString(self):
        result = "Types : " + ABAGAILArrays.toString(self.types)
        result += "\nMax : " + self.max
        result += "\nMin : " + self.min
        if (not self.labelDescription is None):
            result += "\nLabel Description:\n" + self.labelDescription
        
        return result
   