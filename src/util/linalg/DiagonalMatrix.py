
#/**
#* A diagonal matrix is a matrix that only has a diagonal
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class DiagonalMatrix extends Matrix {
#/**
#* The m value
#*/
    int m
#/**
#* The n value
#*/
    int n
#/**
#* The diagonal values
#*/
    double[] diagonal
    
#/**
#* Make a new diagonal matrix
#* @param m the matrix
#*/
     DiagonalMatrix(Matrix m):
        self.m = m.m()
        self.n = m.n()
        self.diagonal = new double[Math.min(m.m(), m.n())]
        for (int i = 0 i < diagonal.length i++):
            diagonal[i] = m.get(i,i)
        }
    }
    
#/**
#* Make a new diagonal matrix
#* @param m the number of rows
#* @param n the number of columns
#* @param diagonal the values
#*/
     DiagonalMatrix(int m, int n, double[] diagonal):
        self.m = m
        self.n = n
        self.diagonal = diagonal
    }

#/**
#* @see util.linalg.Matrix#m()
#*/
     int m():
        return m
    }

#/**
#* @see util.linalg.Matrix#n()
#*/
     int n():
        return n
    }

#/**
#* @see util.linalg.Matrix#get(int, int)
#*/
     double get(int i, int j):
        if (i == j && i < diagonal.length):
            return diagonal[i]
        } else if (i > m || j > n):
            throw new  UnsupportedOperationException()
        }  else {
            return 0
        } 
    }

#/**
#* @see util.linalg.Matrix#set(int, int, double)
#*/
      set(int i, int j, double d):
        if (i == j && i < diagonal.length):
            diagonal[i] = d
        } else if (d != 0 || i > m || j > n){
            throw new UnsupportedOperationException()
        }
    }
    
#/**
#* Get the inverse
#* @return the inverse
#*/
     DiagonalMatrix inverse():
        double[] newDiagonal = new double[diagonal.length]
        for (int i = 0 i < diagonal.length i++):
            newDiagonal[i] = 1/diagonal[i]
        }
        return new DiagonalMatrix(m, n, newDiagonal)
    }
    
#/**
#* Get the square root
#* @return the square root
#*/
     DiagonalMatrix squareRoot():
        double[] newDiagonal = new double[diagonal.length]
        for (int i = 0 i < diagonal.length i++):
            newDiagonal[i] = Math.sqrt(diagonal[i])
        }
        return new DiagonalMatrix(m, n, newDiagonal)
    }

}
