

#/**
#* Testing
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class KMeansClustererTest {
#/**
#* The test main
#* @param args ignored
#*/
     static  main(String[] args) throws Exception {
        Instance[] instances = new Instance[100]
        MultivariateGaussian mga = new MultivariateGaussian(new DenseVector(new double[] {10, 20, 30}), RectangularMatrix.eye(3).times(.5)) 
        MultivariateGaussian mgb = new MultivariateGaussian(new DenseVector(new double[] {-2, -3, -1}), RectangularMatrix.eye(3).times(.4)) 
        for (int i = 0 i < instances.length i++):
            if (Distribution.random.nextBoolean()):
                instances[i] = mga.sample(null)   
            } else {
                instances[i] = mgb.sample(null)
            }
        }
        DataSet set = new DataSet(instances)
        KMeansClusterer km = new KMeansClusterer()
        km.estimate(set)
        System.out.println(km)
    }
}
