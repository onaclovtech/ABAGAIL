

#/**
#* Test the class
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class PruningCriteriaTest {
    
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
        ChiSquarePruningCriteria cspc = new ChiSquarePruningCriteria(1)
        for (int i = 0 i < 4 i++):
            DecisionTreeSplit split = 
                new StandardDecisionTreeSplit(i, 2)
            DecisionTreeSplitStatistics stats = 
                new DecisionTreeSplitStatistics(split, set)
            System.out.println("\nAttribute " + i)
            System.out.println("Should prune? " + cspc.shouldPrune(stats))
        }
    }
}