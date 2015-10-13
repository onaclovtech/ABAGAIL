
#/**
#* An attribute type specifies what type an attribute
#* within a data set is
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class AttributeType:
#/**
#* The binary type
#*/
     # static final AttributeType BINARY = new AttributeType(1)   
# #/**
# #* The integer / discrete type
# #*/
     # static final AttributeType DISCRETE = new AttributeType(2)
# #/**
# #* The continuous type
# #*/
     # static final AttributeType CONTINUOUS = new AttributeType(3)
    
#/**
#* The type of the attribute
#*/
   # int type
    
#/**
#* Make a new attribute type
#* @param t the type of the attribute
#*/
    def __init__(self, t):
        self.type = t
    
#/**
#* @see java.lang.Object#equals(java.lang.Object)
#*/
    def equals(self, o):
        return o.type == self.type
    
    def BINARY():
        return AttributeType(1)
    def DISCRETE():
        return AttributeType(2)
    def CONTINUOUS():
        return AttributeType(3)
#/**
#* @see java.lang.Object#toString()
#*/
    def toString(self):
        if (self.type == 1):
            return "BINARY"
        if (self.type == 2):
            return "DISCRETE"
        if (self.type == 3):
            return "CONTINUOUS"
        return "UNKNOWN"
        