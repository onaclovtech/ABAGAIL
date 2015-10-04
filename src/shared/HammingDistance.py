

#/**
#* The standard hamming distance
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class HammingDistance extends AbstractDistanceMeasure {


#/**
#* @see memory.DistanceMeasure#distanceSquared(double[], double[])
#*/
     double value(Instance va, Instance vb):
        double sum = 0
        for (int i = 0 i < va.size() i++):
            if (va.getDiscrete(i) != vb.getDiscrete(i)):
                sum += 1
            }
        }
        return sum
    }


}
