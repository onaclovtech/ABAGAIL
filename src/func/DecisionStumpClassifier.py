

#/**
#* A decision stump
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class DecisionStumpClassifier extends AbstractConditionalDistribution (FunctionApproximater):
    
#/**
#* The evaluator for deciding on splits
#*/
    SplitEvaluator splitEvaluator
    
#/**
#* The stump itself
#*/
    DecisionTreeNode stump
    
#/**
#* The ranges of the different attributes
#*/
    int[] attributeRanges
    
#/**
#* Create a new decision stump
#* @param splitEvaluator the splitting chooser
#* @param instances the instances to build the tree from
#*/
     DecisionStumpClassifier(SplitEvaluator splitEvaluator):
        self.splitEvaluator = splitEvaluator
    }
    
#/**
#* Create a new decision stump
#*/
     DecisionStumpClassifier():
        self(new InformationGainSplitEvaluator())
    }
    
#/**
#* Estimate from data
#* @param instances the data set
#*/
      estimate(DataSet instances):
        // make the description if it isn't there
        if (instances.getDescription() == null):
            DataSetDescription desc = new DataSetDescription()
            desc.induceFrom(instances)
            instances.setDescription(desc)
        }
        // initialize the ranges
        attributeRanges = new int[instances.getDescription().getAttributeTypes().length]
        for (int i = 0 i < attributeRanges.length i++):
            attributeRanges[i] = instances.getDescription().getDiscreteRange(i)
        }
        // build the stump
        stump = buildStump(instances)
        if (stump == null):
            throw new RuntimeException("Invalid Stump Exception")
        }
    }
    
#/**
#* Build a stump from the instances
#* @param instances the instances to build the stump from
#* @return the stump
#*/
    DecisionTreeNode buildStump(DataSet instances):
        // find the best binary splitter
        DecisionTreeSplit bestSplit = null 
        DecisionTreeSplitStatistics bestStats = null
        double bestValue = Double.NEGATIVE_INFINITY
        for (int i = 0 i < attributeRanges.length i++):
            for (int j = 0 j < attributeRanges[i] j++):
                DecisionTreeSplit split = new BinaryDecisionTreeSplit(i, j)
                DecisionTreeSplitStatistics stats = new DecisionTreeSplitStatistics(split, instances)
                double value = splitEvaluator.splitValue(stats)
                if (value > bestValue):
                    bestValue = value bestSplit = split bestStats = stats
                }
            }
        }
        DecisionTreeNode node = new DecisionTreeNode(bestSplit, bestStats, 
            new DecisionTreeNode[bestStats.getBranchCount()])
        return node
    }

#/**
#* @see dist.ConditionalDistribution#distributionFor(shared.Instance)
#*/
     Distribution distributionFor(Instance instance):
        int branch = stump.getSplit().getBranchOf(instance)
        if (stump.getSplitStatistics().getInstanceCount(branch) == 0):
            return new DiscreteDistribution(stump.getSplitStatistics().getClassProbabilities())
        } else {
            return new DiscreteDistribution(stump.getSplitStatistics().getConditionalClassProbabilities(branch))
        }
    }
    

#/**
#* @see func.FunctionApproximater#value(shared.Instance)
#*/
     Instance value(Instance i):
        return distributionFor(i).mode()
    }

    
#/**
#* Get the stump for the decision tree node
#* @return the stump
#*/
     DecisionTreeNode getStump():
        return stump
    }    
    
#/**
#* Get the split evaluator for the stump
#* @return the evaluator
#*/
     SplitEvaluator getSplitEvaluator():
        return splitEvaluator
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return stump.toString()
    }


}
