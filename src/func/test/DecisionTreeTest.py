

#/**
#* Test the class
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class DecisionTreeTest {
    
#/**
#* Test main
#* @param args ignored
#*/
     static  main(String[] args):
        Instance[] instances =  {
            new Instance(new double[] {0, 0, 0, 1}, 1),
            new Instance(new double[] {1, 0, 0, 0}, 1),
            new Instance(new double[] {1, 0, 0, 0}, 1),
            new Instance(new double[] {1, 0, 0, 0}, 1),
            new Instance(new double[] {1, 0, 0, 1}, 0),
            new Instance(new double[] {1, 0, 0, 1}, 0),
            new Instance(new double[] {1, 0, 0, 1}, 0),
            new Instance(new double[] {1, 0, 0, 1}, 0)
        }
        Instance[] tests =  {
            new Instance(new double[] {0, 1, 1, 1}),
            new Instance(new double[] {0, 0, 0, 0}),
            new Instance(new double[] {1, 0, 0, 0}),
            new Instance(new double[] {1, 1, 1, 1})
        }
        DataSet set = new DataSet(instances)
        PruningCriteria cspc = new ChiSquarePruningCriteria(0)
        SplitEvaluator gse = new GINISplitEvaluator()
        SplitEvaluator igse = new InformationGainSplitEvaluator()
        DecisionTreeClassifier dt = new DecisionTreeClassifier(igse, null, true)
        dt.estimate(set)
        System.out.println(dt)
        for (int i = 0 i < tests.length i++):
            System.out.println(dt.value(tests[i]))
        }
    }
}