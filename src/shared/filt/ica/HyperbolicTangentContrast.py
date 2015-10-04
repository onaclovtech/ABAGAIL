
#/**
#* A log hyperbolic cosine contrast function
#* (the first derivative is hyperbolic tangent)
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class HyperbolicTangentContrast (ContrastFunction):

#/**
#* @see shared.filt.ica.ContrastFunction#g(double)
#*/
     double g(double value):
        double e2x = Math.exp(2 * value)
        if (e2x == Double.POSITIVE_INFINITY):
            return 1
        } else {
            return (e2x - 1) / (e2x + 1)
        }
    }

#/**
#* @see shared.filt.ica.ContrastFunction#gprime(double)
#*/
     double gprime(double value):
        double tanhvalue = g(value)
        return 1 - tanhvalue * tanhvalue
    }

}
