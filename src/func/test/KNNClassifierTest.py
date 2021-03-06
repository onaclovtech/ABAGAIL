



#/**
#* A knn test
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class KNNClassifierTest {
    
#/**
#* The main method
#* @param args ignored
#*/
     static  main(String[] args):
        Instance[] keys = {
            new Instance(new double[] { 1 , 1}),
            new Instance(new double[] { 2 , 2}), 
            new Instance(new double[] { 3 , 3}), 
            new Instance(new double[] { 4 , 4}), 
            new Instance(new double[] { 5 , 5}), 
            new Instance(new double[] { 6 , 6}), 
        }
        
        
        KDTree tree = new KDTree(new DataSet(keys))
        Instance[] results = tree.knn(new Instance(new double[] { 2, 2 }), 4)
        System.out.println(Arrays.asList(results))
    }

}
