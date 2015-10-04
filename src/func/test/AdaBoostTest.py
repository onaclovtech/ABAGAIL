

#/**
#* Test the class
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class AdaBoostTest {
    
#/**
#* Test main
#* @param args ignored
#*/
     static  main(String[] args):
        Instance[] instances =  {
            new Instance(new double[] {1,1,0,0,0,0,0,0}, 0),
            new Instance(new double[] {0,0,1,1,1,0,0,0}, 1),
            new Instance(new double[] {0,0,0,0,1,1,1,1}, 0),
            new Instance(new double[] {1,0,0,0,1,0,1,0}, 1),
            new Instance(new double[] {1,1,1,0,1,1,0,0}, 1),
        }
        Instance[] tests =  {
            new Instance(new double[] {1,1,1,0,0,0,0,0}),
        }
        DataSet set = new DataSet(instances)
        AdaBoostClassifier ds = new AdaBoostClassifier(20, DecisionStumpClassifier.class)
        ds.estimate(set)
        System.out.println(ds)
        for (int i = 0 i < tests.length i++):
            System.out.println(ds.value(tests[i]))
        }
    }
}