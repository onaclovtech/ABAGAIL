

#/**
#* A class representing a lower triangular matrix
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class LowerTriangularMatrix extends Matrix {
	
	/**
	 * The number of rows in the matrix
	 */
	int m
	
	/**
	 * The number of columns in the matrix
	 */
	int n

	/**
	 * The data of the matrix
	 */
	double[][] data

	/**
	 * Create a new square zero matrix that is
	 * restricted to be lower triangular
	 * @param m the row size of the matrix
	 */
	 LowerTriangularMatrix(int m):
		self(m,m)
	}

	/**
	 * Create a new zero matrix that is
	 * restricted to be lower triangular
	 * @param m the row size of the matrix
	 * @param n the column size of the matrix
	 */
	 LowerTriangularMatrix(int m, int n):
		self.m = m
		self.n = n
		data = new double[m][]
		for (int i = 0 i < data.length i++):
			data[i] = new double[Math.min(i + 1, n)]
		}
	}
	
	/**
	 * Create a lower triangular matrix
	 * containing the lower triangular entries
	 * of the given matrix
	 * @param m the matrix to extract from
	 */
	 LowerTriangularMatrix(Matrix m):
		self(m.m(), m.n())
		for (int i = 0 i < m() i++):
			for (int j = 0 j <= i j++):
				set(i,j, m.get(i,j))
			}
		}
	}

	/**
	 * @see linalg.Matrix#m()
	 */
	 int m():
		return m
	}

	/**
	 * @see linalg.Matrix#n()
	 */
	 int n():
		return n
	}

	/**
	 * @see linalg.Matrix#get(int, int)
	 */
	 double get(int i, int j):
		if (i < m() && j < n() && j > i):
			return 0
		} else {
			return data[i][j]
		}
	}

	/**
	 * @see linalg.Matrix#set(int, int, double)
	 */
	  set(int i, int j, double d):
		if (!(i < m() && j < n() && j > i && d == 0)):
			data[i][j] = d
		}
	}
	
	/**
	 * Calculate the determinant
	 * @return the determinant
	 */
	 double determinant():
		int mnmin = Math.min(m(), n())
		double d = 1
		for (int i = 0 i < mnmin i++):
			d *= get(i,i)
		}
		return d
	}
	
	/**
	 * @see linalg.Matrix#transpose()
	 */
	 Matrix transpose():
		UpperTriangularMatrix result = new UpperTriangularMatrix(n(), m())
		for (int i = 0 i < data.length i++):
			for (int j = 0 j < data[i].length j++):
				result.set(j, i, data[i][j])
			}
		}
		return result
	}
	
	/**
	 * Solve self upper triangular system for the
	 * given vector.  Solves A*x = b for the given
	 * b.
	 * @param b the vector to solve for
	 * @return the solution vector
	 */
	 Vector solve(Vector b):
		b = (Vector) b.copy()
		// solve by forward substiution 
		// overwriting the copy of b with the solution x
		b.set(0, b.get(0) / get(0,0))
		for (int i = 1 i < b.size() i++):
			double sum = 0
			for (int j = 0 j < i j++):
				sum += get(i, j) * b.get(j)
			}
			b.set(i, (b.get(i) - sum) / get(i,i))
		}
		return b
	}
    
#/**
#* Find the inverse of self matrix
#* @return the inverse
#*/
     LowerTriangularMatrix inverse():
        Vector[] columns = new Vector[n]
        for (int i = 0 i < columns.length i++):
            columns[i] = solve(DenseVector.e(i, m))
        }
        return new LowerTriangularMatrix(
            RectangularMatrix.columns(columns))
    }
	
	/**
	 * @see linalg.Matrix#copy()
	 */
	 Copyable copy():
		LowerTriangularMatrix result = new LowerTriangularMatrix(m(), n())
		for (int i = 0 i < data.length i++):
			for (int j = 0 j < data[i].length j++):
				result.data[i][j] = data[i][j]		
			}
		}
		return result
	}

}
