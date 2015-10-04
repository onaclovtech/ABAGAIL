

#/**
#* A test for lower triangular matrices
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class LowerTriangularMatrixTest {

#/**
#* Test main,
#* @param args ignored
#*/
     static  main(String[] args):
      double[][] a = {
          { 1, 0, 0, 0 },
          { 3, 5, 0, 0 },
          { 4, 3, 6, 0 },
          { 1, 2, 3, 4 }
      }

      LowerTriangularMatrix lm = new LowerTriangularMatrix(new RectangularMatrix(a))    
      System.out.println(lm)
      System.out.println(lm.inverse())
      System.out.println(lm.inverse().times(lm))
      System.out.println(lm.times(lm.inverse()))
    }

}
