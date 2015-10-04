



#/**
#* A HyperRectangle class for a KDTree implementation
#* @author Andrew Guillory
#* @version 1.0
#*/
 class HyperRectangle (Copyable):

#/**
#* The min values of the rectangle
#*/
    Vector min

#/**
#* The max values of the rectangle
#*/
    Vector max

#/**
#* Construct a new hyper rectangle
#* @param min the array of minimum values
#* @param max the array of maximum values
#*/
     HyperRectangle(Vector min, Vector max):
        self.min = min
        self.max = max
    }

#/**
#* Create a new infinite hyper rectangle
#* @param k the dimensionality
#*/
     HyperRectangle(int k):
        double[] maxd = new double[k]
        Arrays.fill(maxd, Double.POSITIVE_INFINITY)
        max = new DenseVector(maxd)
        double[] mind = new double[k]
        Arrays.fill(mind, Double.NEGATIVE_INFINITY)
        min = new DenseVector(mind)
    }

#/**
#* Get the minimum values
#* @return the minimum values
#*/
     Vector getMinimumValues():
        return min
    }

#/**
#* Set the minimum values
#* @param min the min values
#*/
      setMinimumValues(Vector min):
        self.min = min
    }

#/**
#* Get the minimum values
#* @return the minimum values 
#*/
     Vector getMaximumValues():
        return max
    }

#/**
#* Set the maximum values
#* @param max the maximum values
#*/
      setMaximumValues(Vector max):
        self.max = max
    }

#/**
#* Get the hyper rectangle split to the left
#* @return the rectangle
#*/
     HyperRectangle splitLeft(double value, int dimension):
        HyperRectangle clone = (HyperRectangle) copy()
        clone.getMaximumValues().set(dimension, value)
        return clone
    }

#/**
#* Get a hyper rectangle split to the right
#* @return the rectangle
#*/
     HyperRectangle splitRight(double value, int dimension):
        HyperRectangle clone = (HyperRectangle) copy()
        clone.getMinimumValues().set(dimension, value)
        return clone
    }

#/**
#* Get the point in self hyper cube nearest to the target
#* @param target the point you are looking for
#* @return the point nearest to the target
#*/
     Instance pointNearestTo(Instance target):
        double[] nearest = new double[target.size()]
        for (int i = 0 i < nearest.length i++):
            if (target.getContinuous(i) <= min.get(i)):
                nearest[i] = min.get(i)
            } else if (target.getContinuous(i) >= max.get(i)):
                nearest[i] = max.get(i)
            } else {
                nearest[i] = target.getContinuous(i)
            }
        }
        return new Instance(new DenseVector(nearest))
    }
    
#/**
#* Make a copy of self recangle
#* @return the copy
#*/
     Copyable copy():
        return new HyperRectangle((Vector) min.copy(), (Vector) max.copy())
    }
}
