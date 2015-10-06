


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
     def __init__ (self, data, label = None, weight = 1.0):
        self.data = data
        self.label = label
        self.weight = weight
    
    
# TRANSLATE THE FOLLOWING TO PYTHON
    #/**
#* Make a instance
#* @param ds the data
#*/
     # Instance(double[] ds):
        # data = DenseVector(ds)
        # weight = 1.0
    # }
    
# #/**
# #* Make a instance with the given value
# #* @param val the value
# #*/
     # Instance(double val):
        # data = DenseVector(1)
        # data.set(0, val)
        # weight = 1.0
    # }
    
# #/**
# #* Make a instance with the given value
# #* @param val the value
# #*/
     # Instance(int val):
        # data = DenseVector(1)
        # data.set(0, val)
        # weight = 1.0
    # }
    
# #/**
# #* Make a discrete input output instance
# #* @param i the input
# #* @param o the output
# #*/
     # Instance(int i, int o):
        # self(i)
        # label = Instance(o)
    # }

# #/**
# #* Make a double input discrete output
# #* @param ds the input
# #* @param i the output
# #*/
     # Instance(double[] ds, int i):
        # self(ds)
        # label = Instance(i)
    # }

# #/**
# #* Make a input output instance
# #* @param ds the data
# #* @param b the label
# #*/
     # Instance(double[] ds, boolean b):
        # self(ds)
        # label = Instance(b)
    # }

    
    
# #/**
# #* Make a instance with the given boolean value
# #* @param val the value
# #*/
     # Instance(boolean val):
        # self(val ? 1 : 0)
    # }
    
#/**
#* Get the size of the instance
#* @return the size
#*/
     def size(self):
        return len(self.data)
    
#/**
#* Get the ith continuous value
#* @param i the value to get
#* @return the value
#*/
     def getContinuous(self, i=0):
        return self.data[i]
    
    
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
        return self.label
    
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
     def copy():
        if (label != null):
            return Instance(data.copy(), label.copy(), weight)
        else:
            return Instance(data.copy(), null, weight)
        
    
    
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
    



