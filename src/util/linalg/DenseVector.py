from src.util.linalg.Vector import *

#/**
#* An implementation of a vector that is dense
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class DenseVector(Vector):
    
#/**
#* The data
#*/
    #double[] data
    
#/**
#* Make a new dense vector
#* @param data the data
#*/
     def __init__(self, data = None, size = None):
        #print "denseVector.init.data.type" + str(type(data))
        if data:
            if not isinstance(data, list):
                raise TypeError('You fail')
            self.data = data
        else:
            self.data = [None] * size
    
     def copy(self):
        return DenseVector(data = Vector.copy(self))
   

#/**
#* @see linalg.Vector#size()
#*/
     def size(self):
        return len(self.data)
    

#/**
#* @see linalg.Vector#get(int)
#*/
     def get(self, i):
        #print "get.data.type: " + str(type(self.data))
        return self.data[i]
    
    
#/**
#* @see linalg.Vector#set(int, double)
#*/
     def set(self, i,  value):
        self.data[i] = value
    
    
#/**
#* Make an identity vector 
#* @param i the dimension of identity
#* @param size the size of the vector
#* @return the identity vector
#*/
     def e(self, i, size):
        result = [size]
        result[i] = 1
        return DenseVector(result)
    
    
#/**
#* Get the identity 1 vector of the given size
#* @param size the size
#* @return the identity vector
#*/
     def e(self, size):
        return e(0, size)
    