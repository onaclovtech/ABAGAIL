#/**
#* A class representing a vector with linear algebra
#* operations.
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class Vector:
    

#/**
#* Get the size of the vector (the number of rows)
#* @return the number of rows
#*/
    # abstract int size()
    
#/**
#* Get an element from the vecotr
#* @param i the element to get
#* @return the element
#*/
    # abstract double get(int i)
    
#/**
#* Get some sub portion of the vector
#* @param ia the starting index (inclusive)
#* @param ib the ending index (exclusive)
#* @return the result
#*/
     def get(self, ia, ib):
        result = [ib - ia]
        for i in len(result):
            result[i] = get(ia + i)
        
        return DenseVector(result)
    
    
#/**
#* Set a portion of the vector
#* @param i the starting porition
#* @param values the values
#*/
     def set(self, i, values):
        #for row = i row-i < values.size() row++):
        for row in range(i,values.size): # This needs fixing
            self.set(row, values.get(row-i))
     
   
#/**
#* Remove a column from the middle of the vector and return a new vector
#* 
#* @param i
#*/
     def remove(self, inx):
        data = [self.size()]
        for i in range(len(data)):
            data[i] = self.get(i)
       
        result = [size() - 1]
# Find Python Equivalent
#        System.arraycopy(data, 0,       result, 0,   inx)
#        System.arraycopy(data, inx + 1, result, inx, size() - inx - 1)
        
        return DenseVector(result)
    
#/**
#* Get the maximum of self vector with the given vector
#* @param v the other vector
#* @return the max
#*/
     def max(self, v):
        result = [self.size()]
        for i in range(len(result)):
            result[i] = max(self.get(i), v.get(i))
        return DenseVector(result)
    
#/**
#* Set self vector equal to the max of itself with 
#* the given vector
#* @param v the given vector
#*/
     def maxEquals(self, v):
        for i in range(self.size()):
            self.set(i, max(self.get(i), v.get(i)))

 
#/**
#* Set self vector equal to the min of itself with 
#* the given vector
#* @param v the given vector
#*/
     def minEquals(self, v):
        for i in range(self.size()):
            self.set(i, min(self.get(i), v.get(i)))
   
    
#/**
#* Get the minimum of self vector with the given vector
#* @param v the other vector
#* @return the min
#*/
     def min(self, v):
        result = [self.size()]
        for i in range(len(result)):
            result[i] = min(self.get(i), v.get(i))
        return DenseVector(result)
    
    
#/**
#* Get the indice arg max of self vector
#* @return the arg max inidice
#*/
     def argMax(self):
        max = 0
        for i in range(1,self.size()):
            if (self.get(i) > self.get(max)):
                max = i
        return max
    
#/**
#* Dot product self vector with another vector
#* @param vector the other vector
#* @return the dot product
#*/
     def dotProduct(self, vector):
        result = 0
        for i in range(self.size()):
            result += self.get(i) * vector.get(i)   
        
        return result
    

#/**
#* Outer product self vector with another vector
#* @param vector the other vector
#* @return the outer product
#*/    
     # Matrix outerProduct(Vector vector):
        # double[][] result = new double[size()][size()]
        # for (int i = 0 i < result.length i++):
            # for (int j = 0 j < result[0].length j++):
                # result[i][j] = get(i) * vector.get(j)
            # }
        # }
        # return new RectangularMatrix(result)
    # }
    
# #/**
# #* Multiply self vector by a scale
# #* @param scale the scale
# #* @return the multiplied vector
# #*/
     # Vector times(double scale):
        # Vector result = (Vector) copy()
        # result.timesEquals(scale)
        # return result
    # }
    
# #/**
# #* Multiply self vector by a scale in place
# #* @param scale the scale
# #*/
      # timesEquals(double scale):
    	# for (int i = 0 i < size() i++):
    		# set(i, get(i) * scale)
    	# }
    # }
    
# #/**
# #* Add self vector to another vector
# #* @param vector the other vector
# #* @return the result
# #*/
     # Vector plus(Vector vector):
      	# Vector result = (Vector) copy()
      	# result.plusEquals(vector)
      	# return result
    # }
    
# #/**
# #* Get the sum of all of the entries
# #* @return the sum
# #*/
     # double sum():
        # double sum = 0
        # for (int i = 0 i < size() i++):
            # sum += get(i)
        # }
        # return sum
    # }
	
	# /**
	 # * Add a vector onto self vector in place
	 # * @param vector the vector to add
	 # */
	  # plusEquals(Vector vector):
		# for (int i = 0 i < size() i++):
			# set(i, get(i) + vector.get(i))
		# }
	# }

# #/**
# #* Subtract a vector from self vector
# #* @param vector the other vector
# #* @return the result
# #*/
     # Vector minus(Vector vector):
    	# Vector result = (Vector) copy()
    	# result.minusEquals(vector)
    	# return result
    # }

	# /**
	 # * Subtract a vector from self vector in place
	 # * @param vector the vector to subtract
	 # */
	  # minusEquals(Vector vector):
		# for (int i = 0 i < size() i++):
			# set(i, get(i) - vector.get(i))
		# }
	# }
    
# #/**
# #* Get the two norm squared of self vector
# #* @return the two norm squared
# #*/
     # double normSquared():
        # return self.dotProduct(self)
    # }

# #/**
# #* Get the two norm of self vector
# #* @return the two norm 
# #*/
     # double norm():
        # return Math.sqrt(normSquared())
    # }


	# /**
	 # * Make a copy of self vector
	 # * @return the copy
	 # */
	 # Copyable copy():
		# double[] copy = new double[size()]
		# for (int i = 0 i < copy.length i++):
			# copy[i] = get(i)
		# }
		# return new DenseVector(copy)
	# }

# #/**
# #* @see java.lang.Object#equals(java.lang.Object)
# #*/
     # boolean equals(Object o):
       # Vector v = (Vector) o
       # if (v.size() != size()):
           # return false
       # }
       # for (int i = 0 i < v.size() i++):
            # if (get(i) != v.get(i)):
                # return false
            # }
       # }
       # return true
    # }
    
# #/**
# #* @see java.lang.Object#toString()
# #*/
     # String toString():
        # DecimalFormat df = new DecimalFormat("0.000000")
        # String result = ""
        # for (int i = 0 i < size() i++):
            # result += df.format(get(i))
            # if (i + 1 < size()):
                # result += ", "
            # }
        # }
        # return result
    # }

# }


