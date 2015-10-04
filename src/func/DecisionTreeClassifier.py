

#/**
#* A class implementing a decision tree
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class DecisionTreeClassifier extends AbstractConditionalDistribution (FunctionApproximater):
    
#/**
#* The evaluator for deciding on splits
#*/
    SplitEvaluator splitEvaluator
    
#/**
#* Whether or not to prune
#*/
    PruningCriteria pruningCriteria
    
#/**
#* The root node in the tree
#*/
    DecisionTreeNode root
    
#/**
#* Whether or not to use binary splits
#*/
    boolean useBinarySplits
    
#/**
#* The ranges of the different attributes
#*/
    int[] attributeRanges
    
#/**
#* The range of the classifications
#*/
    int classRange
    
#/**
#* Create a new decision tree
#* @param splitEvaluator the splitting chooser
#* @param pruningCriteria the criteria for prunning
#* @param useBinarySplits whether or not to use binary splits
#* @param instances the instances to build the tree from
#*/
     DecisionTreeClassifier(SplitEvaluator splitEvaluator, PruningCriteria pruningCriteria,
            boolean useBinarySplits):
        self.splitEvaluator = splitEvaluator
        self.pruningCriteria = pruningCriteria
        self.useBinarySplits = useBinarySplits
    }
    
#/**
#* Create a new decision tree with no prunning
#* @param splitEvaluator the splitting chooser
#* @param useBinarySplits whether or not to use binary splits
#* @param instances the instances to build the tree from
#*/
     DecisionTreeClassifier(SplitEvaluator splitEvaluator,
            boolean useBinarySplits):
        self(splitEvaluator, null, useBinarySplits)
    }

#/**
#* Create a new decision tree with no prunning
#* @param instances the instances to build the tree from
#*/
     DecisionTreeClassifier():
        self(new InformationGainSplitEvaluator(), null, false)
    }
    
    
#/**
#* Estimate from the given data set
#* @param set the set
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
        // build the tree
        root = buildTree(instances)
        // if the root is pruned, use a stump why not?
        if (root == null):
            DecisionStumpClassifier stump = new DecisionStumpClassifier(splitEvaluator)
            stump.estimate(instances)
            root = stump.getStump()
        }
    }
    
#/**
#* Build a tree from the given instances
#* @param instances the instances to build the tree from
#* @return the tree
#*/
    DecisionTreeNode buildTree(DataSet instances):
        // nothing left in the tree
        if (instances.size() == 0):
            return null
        } 
        // check if all of the same class
        boolean allOfSameClass = true
        int sameClass = instances.get(0).getLabel().getDiscrete()
        for (int i = 0 i < instances.size() && allOfSameClass i++):
            allOfSameClass = instances.get(i).getLabel().getDiscrete() == sameClass
        }
        if (allOfSameClass):
            return null
        }
        // find the best splitter
        DecisionTreeSplit bestSplit = null DecisionTreeSplitStatistics bestStats = null
        double bestValue = Double.NEGATIVE_INFINITY
        if (!useBinarySplits):
            for (int i = 0 i < attributeRanges.length i++):
                DecisionTreeSplit split = new StandardDecisionTreeSplit(i, attributeRanges[i])
                DecisionTreeSplitStatistics stats = new DecisionTreeSplitStatistics(split, instances)
                double value = splitEvaluator.splitValue(stats)
                if (value > bestValue):
                    bestValue = value bestSplit = split bestStats = stats 
                }
            }
        } else {
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
        }
        // divide up the instances
        Instance[][] divided = new Instance[bestSplit.getNumberOfBranches()][]
        // check for at least two non zero branches
        int nonZero = 0
        for (int i = 0 i < divided.length i++):
            divided[i] = new Instance[bestStats.getInstanceCount(i)] 
            if (divided[i].length != 0):
                nonZero++
            }
        }
        if (nonZero < 2):
            return null
        }
        // recursive step
        int[] counters = new int[divided.length]
        for (int i = 0 i < instances.size() i++):
            int branch = bestSplit.getBranchOf(instances.get(i))
            divided[branch][counters[branch]] = instances.get(i)
            counters[branch]++
        }
        DecisionTreeNode[] nodes = new DecisionTreeNode[divided.length]
        for (int i = 0 i < nodes.length i++):
            DataSet newSet = new DataSet(divided[i], instances.getDescription())
            nodes[i] = buildTree(newSet)
        }
        DecisionTreeNode node = new DecisionTreeNode(bestSplit, bestStats, nodes)
        if (node.isLeaf() && pruningCriteria != null && pruningCriteria.shouldPrune(bestStats)):
            return null
        }
        return node
    }

#/**
#* Get the class distribution for an instance
#* @param instance the instance to classify
#* @return the distribution
#*/
     Distribution distributionFor(Instance instance):
        DecisionTreeNode node = root
        while (node.getNode(node.getSplit().getBranchOf(instance)) != null):
            node = node.getNode(node.getSplit().getBranchOf(instance))
        }
        int branch = node.getSplit().getBranchOf(instance)
        if (node.getSplitStatistics().getInstanceCount(branch) == 0):
            return new DiscreteDistribution(
                node.getSplitStatistics().getClassProbabilities())
        } else {
            return new DiscreteDistribution(
                node.getSplitStatistics().getConditionalClassProbabilities(branch))
        }
    }
    
#/**
#* Get the classifiation for an instance
#* @param instance the instance to classify
#* @return the classification
#*/
     Instance value(Instance instance):
        return distributionFor(instance).mode()
    }
    
    
#/**
#* Get the root node
#* @return the root
#*/
     DecisionTreeNode getRoot():
        return root
    }   

#/**
#* Get the split evaluator for the stump
#* @return the evaluator
#*/
     SplitEvaluator getSplitEvaluator():
        return splitEvaluator
    }
    
#/**
#* Get the prunning criteria
#* @return the prunning criteria
#*/
     PruningCriteria getPruningCriteria():
        return pruningCriteria
    }

#/**
#* Does the tree use binary splits
#* @return true if it should
#*/
     boolean isUseBinarySplits():
        return useBinarySplits
    }
    
#/**
#* Set the pruning criteria
#* @param criteria the pruning criteria
#*/
      setPruningCriteria(PruningCriteria criteria):
        pruningCriteria = criteria
    }

#/**
#* Set the split evaluator
#* @param evaluator the split evaluator
#*/
      setSplitEvaluator(SplitEvaluator evaluator):
        splitEvaluator = evaluator
    }

#/**
#* Set whether to use binary splits
#* @param b true if we should
#*/
      setUseBinarySplits(boolean b):
        useBinarySplits = b
    }
    
#/**
#* Get the height of the tree
#* @return the height
#*/
     int getHeight():
        return height(root)
    }
    
#/**
#* Get the height of the tree
#* @param root the root node
#* @return the height
#*/
    int height(DecisionTreeNode root):
        if (root == null):
            return 0
        }
        int height = 1
        for (int i = 0 i < root.getNodes().length i++):
            height = Math.max(height, 1 + height(root.getNode(i)))
        }
        return height
    }

#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return root.toString()
    }



}
