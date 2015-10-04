

#/**
#* Test the class
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class GaussianProcessRegressionTest {
    
#/**
#* Test main
#* @param args ignored
#*/
     static  main(String[] args):
        Instance[] instances =  {
            new Instance(new double[] {1}, -1),
            new Instance(new double[] {1}, -1),
            new Instance(new double[] {1}, -1),
            new Instance(new double[] {1}, -1),
            new Instance(new double[] {-1}, 1),
            new Instance(new double[] {-1}, 1),
            new Instance(new double[] {-1}, 1),
            new Instance(new double[] {-1}, 1)
        }
        Instance[] tests =  {
            new Instance(new double[] {-1}),
            new Instance(new double[] {-1}),
            new Instance(new double[] {1}),
            new Instance(new double[] {1})
        }
        DataSet set = new DataSet(instances)
        GaussianProcessRegression gp = new GaussianProcessRegression(
           new LinearKernel(), .01)
        gp.estimate(set)
        System.out.println(gp)
        for (int i = 0 i < tests.length i++):
            System.out.println(gp.value(tests[i]))
        }
    }
}