


#/**
#* A class representing a matrix, with linear algebra operations
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 abstract class Matrix (Serializable), Copyable {
    
    
#/**
#* Get the number of rows
#* @return the number of rows
#*/
     abstract int m()
        
#/**
#* Get the number of columns
#* @return the number of colulmns
#*/
     abstract int n()
        
#/**
#* Get a value
#* @param i the row
#* @param j the column
#* @return the value
#*/
     abstract double get(int i, int j)
        
#/**
#* Get a sub matrix from self matrix
#* @param ia the starting row index (inclusive)
#* @param ib the ending row index (exclusive)
#* @param ja the starting column index (inclusive)
#* @param jb the ending column index(exclusive)
#* @return the sub matrix
#*/
     Matrix get(int ia, int ib, int ja, int jb):
        double[][] result = new double[ib - ia][jb - ja]
        for (int i = 0 i < result.length i++):
            for (int j = 0 j < result[0].length j++):
                result[i][j] = get(ia + i, ja + j)
            }
        }
        return new RectangularMatrix(result)
    }
    
#/**
#* Set a value
#* @param i the row
#* @param j the column
#* @param d the new value
#*/
     abstract  set(int i, int j, double d)
     
#/**
#* Set a block in self matrix equal to the given matrix
#* @param i the top row of the block
#* @param j the left most column of the block
#* @param matrix the values to set the block with
#*/
      set(int i, int j, Matrix matrix):
        for (int row = i row < matrix.m() + i row++):
            for (int column = j column < matrix.n() + j column++):
                set(row, column, matrix.get(row - i,column - j))
            }
        }
    }
    
#/**
#* Create the transpose of self matrix\
#* @return the transpose
#*/
     Matrix transpose():
        double[][] result = new double[n()][m()]
        for (int i = 0 i < result.length i++):
            for (int j = 0 j < result[i].length j++):
                result[i][j] = get(j, i)
            }
        }
        return new RectangularMatrix(result)
    }

#/**
#* Get a column vector from self matrix
#* @param index the index of the column to get
#* @return the column vector
#*/
     Vector getColumn(int index):
        double[] result = new double[m()]
        for (int i = 0 i < result.length i++):
            result[i] = get(i, index)
        }
        return new DenseVector(result)
    }
    
#/**
#* Set a column of self matrix
#* @param index the index
#* @param v the vector
#*/
      setColumn(int index, Vector v):
        for (int i = 0 i < v.size() i++):
            set(i, index, v.get(i))
        }
    }

#/**
#* Get a row vector from the matrix
#* @param index the index of the row to get
#* @return the row vector
#*/
     Vector getRow(int index):
        double[] result = new double[n()]
        for (int i = 0 i < result.length i++):
            result[i] = get(index, i)
        }
        return new DenseVector(result)
    }

    
#/**
#* Set a row of self matrix
#* @param index the index
#* @param v the vector
#*/
      setRow(int index, Vector v):
        for (int i = 0 i < v.size() i++):
            set(index, i, v.get(i))
        }
    }

    
#/**
#* Multiply self matrix with another matrix
#* @param matrix the other matrix
#* @return the resulting matrix
#*/
     Matrix times(Matrix matrix):
        double[][] result = new double[m()][matrix.n()]
        for (int row = 0 row < result.length row++):
            for (int column = 0 column < result[0].length column++):
                for (int i = 0 i < n() i++):
                    result[row][column] += 
                        get(row,i) * matrix.get(i, column)   
                }
            }
        }
        return new RectangularMatrix(result)
    }
    
    
#/**
#* Multiply with a vector
#* @param vector the vector to multiply by
#* @return the result
#*/
     Vector times(Vector vector):
        double[] result = new double[m()]
        for (int row = 0 row < result.length row++):
            for (int i = 0 i < n() i++):
                result[row] += get(row, i) * vector.get(i) 
            }
        }
        return new DenseVector(result)
    }
    
#/**
#* Multiply the matrix by a scale
#* @param scale the scale
#* @return the scaled matrix
#*/
     Matrix times(double scale):
        Matrix result = (Matrix) copy()
        result.timesEquals(scale)
        return result
    }
    
#/**
#* Multiply self matrix in place by the given scale
#* @param scale the scale to multiply by
#*/
      timesEquals(double scale):
    	for (int i = 0 i < m() i++):
    		for (int j = 0 j < n() j++):
    			set(i, j, get(i,j) * scale)	
    		}
    	}
    }
    
#/**
#* Add self matrix with another matrix
#* @param matrix the other matrix
#* @return the resulting matrix
#*/
     Matrix plus(Matrix matrix):
      	double[][] result = new double[m()][n()]
      	for (int i = 0 i < result.length i++):
      		for (int j = 0 j < result[i].length j++):
      			result[i][j] = get(i,j) + matrix.get(i,j)
      		}
      	}
      	return new RectangularMatrix(result)
    }
    
#/**
#* Add self matrix with another matrix in place
#* @param matrix the other matrix to add
#*/
      plusEquals(Matrix matrix):
		for (int i = 0 i < m() i++):
			for (int j = 0 j < n() j++):
				set(i,j, get(i,j) + matrix.get(i,j))	
			}
		}
    }
    
#/**
#* Subtract self matrix with another matrix
#* @param matrix the other matrix
#* @return the resulting matrix
#*/
     Matrix minus(Matrix matrix):
		double[][] result = new double[m()][n()]
		for (int i = 0 i < result.length i++):
			for (int j = 0 j < result[i].length j++):
				result[i][j] = get(i,j) - matrix.get(i,j)
			}
		}
		return new RectangularMatrix(result)    }
    
#/**
#* Subtract from self matrix in place
#* @param matrix the matrix to subtract
#*/
      minusEquals(Matrix matrix):
    	for (int i = 0 i < m() i++):
    		for (int j = 0 j < n() j++):
    			set(i,j, get(i,j) - matrix.get(i,j))
    		}
    	}
    }
    
#/**
#* Create and return a copy of self matrix
#* @return the copy
#*/
     Copyable copy():
        double[][] result = new double[m()][n()]
        for (int i = 0 i < result.length i++):
            for (int j = 0 j < result[0].length j++):
                result[i][j] = get(i,j)
            }
        }
        return new RectangularMatrix(result)
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        DecimalFormat df = new DecimalFormat("0.000000")
        String result = ""
        for (int i = 0 i < m() i++):
            for (int j = 0 j < n() j++):
                 result += df.format(get(i,j)) + "\t"
            }
            result += "\n"
        }
        return result
    }
    

}