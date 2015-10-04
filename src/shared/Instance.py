


#/**
#* The abstract class representing some instance.
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class Instance (Serializable), Copyable {

#/**
#* The label for self instance
#*/
    Instance label
    
#/**
#* The vector storing the data
#*/
    Vector data
    
#/**
#* The weight of the instance
#*/
    double weight
#/**
#* Make a new instance from the given data
#* @param data the data itself
#* @param label the label
#* @param weight the weight
#* @param dataSet the data set
#*/
     Instance(Vector data, Instance label, double weight):
        self.data = data
        self.label = label
        self.weight = weight
    }
    
#/**
#* Make a new instance from the given data
#* @param data the data itself
#* @param label the label
#*/
     Instance(Vector data, Instance label):
        self.data = data
        self.label = label
        self.weight = 1.0
    }
    
#/**
#* Make a new instance using the given vector
#* @param v the vector of data
#*/
     Instance(Vector v):
        data = v
        weight = 1.0
    }
    
#/**
#* Make a new instance
#* @param ds the data
#*/
     Instance(double[] ds):
        data = new DenseVector(ds)
        weight = 1.0
    }
    
#/**
#* Make a new instance with the given value
#* @param val the value
#*/
     Instance(double val):
        data = new DenseVector(1)
        data.set(0, val)
        weight = 1.0
    }
    
#/**
#* Make a new instance with the given value
#* @param val the value
#*/
     Instance(int val):
        data = new DenseVector(1)
        data.set(0, val)
        weight = 1.0
    }
    
#/**
#* Make a new discrete input output instance
#* @param i the input
#* @param o the output
#*/
     Instance(int i, int o):
        self(i)
        label = new Instance(o)
    }

#/**
#* Make a new double input discrete output
#* @param ds the input
#* @param i the output
#*/
     Instance(double[] ds, int i):
        self(ds)
        label = new Instance(i)
    }

#/**
#* Make a new input output instance
#* @param ds the data
#* @param b the label
#*/
     Instance(double[] ds, boolean b):
        self(ds)
        label = new Instance(b)
    }

    
    
#/**
#* Make a new instance with the given boolean value
#* @param val the value
#*/
     Instance(boolean val):
        self(val ? 1 : 0)
    }
    
#/**
#* Get the size of the instance
#* @return the size
#*/
     int size():
        return data.size()
    }
    
#/**
#* Get the ith continuous value
#* @param i the value to get
#* @return the value
#*/
     double getContinuous(int i):
        return data.get(i)
    }
    
#/**
#* Get the ith discrete value
#* @param i the value to get
#* @return the value
#*/
     int getDiscrete(int i):
        return (int) Math.round(data.get(i))
    }
    
#/**
#* Get the continuous value of self instance
#* @return the value
#*/
     double getContinuous():
        return getContinuous(0)
    }
    
#/**
#* Get the discrete value of self instance
#* @return the discrete value
#*/
     int getDiscrete():
        return getDiscrete(0)
    }
    

#/**
#* Get a plus or minus value
#* @return a plus or minus boolean value
#*/
     double getPlusMinus():
        return getDiscrete() == 1 ? 1 : -1
    }
    
#/**
#* Get the boolean value
#* @return the boolen value
#*/
     boolean getBoolean():
        return getDiscrete() == 1
    }
    
#/**
#* Get the label for self instance
#* @return the label
#*/
     Instance getLabel():
        return label
    }
#/**
#* Get the data vector
#* @return the data
#*/
     Vector getData():
        return data
    }

#/**
#* Get the weight of self instance
#* @return the weight
#*/
     double getWeight():
        return weight
    }

#/**
#* Set the data vector
#* @param vector the data vector
#*/
      setData(Vector vector):
        data = vector
    }

#/**
#* Set the label for self instance
#* @param instance the label
#*/
      setLabel(Instance instance):
        label = instance
    }

#/**
#* Set the weight for the instance
#* @param d the new weight
#*/
      setWeight(double d):
        weight = d
    }
    
#/**
#* Make a new instance
#* @return the copy
#*/
     Copyable copy():
        if (label != null):
            return new Instance((Vector) data.copy(), (Instance) label.copy(), weight)
        } else {
            return new Instance((Vector) data.copy(), null, weight)
        }
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        String result = data.toString()
        if (label != null):
            result += " : " + label.toString()
        }
        if (weight != 1.0):
            result += " x " + weight
        }
        return result
    }


}
