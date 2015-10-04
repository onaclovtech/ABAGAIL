
#/**
#* An abstract error measure
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 abstract class AbstractErrorMeasure (ErrorMeasure):
#/**
#* Calculate the error between two data sets
#* @param a the first
#* @param b the second
#* @return the error
#*/
     double value(DataSet a, DataSet b):
        double error = 0
        for (int i = 0 i < a.size() i++):
            error += value(a.get(i), b.get(i))
        }
        return error
    }
}
