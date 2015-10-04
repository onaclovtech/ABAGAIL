

#/**
#* A distance measure that mixes
#* several distance measures
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class MixedDistanceMeasure extends AbstractDistanceMeasure{
    
#/**
#* The distance measure for each attribute
#*/
    AttributeType[] types
    
#/**
#* Make a new mixed distance measure
#* @param measures the measures to use
#*/
     MixedDistanceMeasure(AttributeType[] types):
       self.types = types
    }

#/**
#* @see memory.DistanceMeasure#distance(double[], double[])
#*/
     double value(Instance va, Instance vb):
        double distance = 0
        for (int i = 0 i < va.size() i++):
            if (types[i] == AttributeType.CONTINUOUS):
                distance += (va.getContinuous(i) - vb.getContinuous(i)) 
#* (va.getContinuous(i) - vb.getContinuous(i))
            } else {
                if (va.getDiscrete(i) != vb.getDiscrete(i)):
                    distance += 1
                }
            }
        }
        return distance
    }

}

