

#/**
#* Test the class
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class SplitEvaluatorTest {
    
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
        DataSet set = new DataSet(instances)
        set.setDescription(new DataSetDescription(set))
        InformationGainSplitEvaluator ie = new InformationGainSplitEvaluator()
        GINISplitEvaluator ge = new GINISplitEvaluator()
        for (int i = 0 i < 4 i++):
            DecisionTreeSplit split = 
                new StandardDecisionTreeSplit(i, 2)
            DecisionTreeSplitStatistics stats = 
                new DecisionTreeSplitStatistics(split, set)
            System.out.println("\nAttribute " + i)
            System.out.println("Information gain: " + ie.splitValue(stats))
            System.out.println("GINI index: " + ge.splitValue(stats))
        }
    }
}
