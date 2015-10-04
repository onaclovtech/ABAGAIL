

#/**
#* A knn classifier
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class KNNClassifier extends AbstractConditionalDistribution (FunctionApproximater):
    
#/**
#* The distance measure
#*/
    DistanceMeasure distanceMeasure
    
#/**
#* The range limit for the neighbors
#*/
    double range
    
#/**
#* The number of neighbors
#*/
    int k
    
#/**
#* Whether or not to weight by distance
#*/
    boolean weightByDistance
    
#/**
#* The range of classes
#*/
    int classRange
    
#/**
#* The tree
#*/
    KDTree tree
    
#/**
#* Make a new knn classifier
#*/
     KNNClassifier():
        self(1, new EuclideanDistance())
    }
    
#/**
#* Build a new classifier
#* @param examples the examples
#* @param k the k value
#* @param measure the distance measure
#*/
     KNNClassifier(int k,
            DistanceMeasure measure):
        self(k, false, measure, -1)
    }
    
#/**
#* Build a new classifier
#* @param examples the examples
#* @param k the k value
#* @param weight the weight
#* @param measure the distance measure
#*/
     KNNClassifier(int k, boolean weight,
            DistanceMeasure measure):
        self(k, weight, measure, -1)
    }
    
#/**
#* Build a new classifier
#* @param examples the examples
#* @param k the k value
#* @param weight the weight
#* @param measure the distance measure
#* @param range the range
#*/
     KNNClassifier(int k, boolean weight,
            DistanceMeasure measure, double range):
        self.k = k
        self.weightByDistance = weight
        self.range = range
        self.distanceMeasure = measure

    }
    
#/**
#* Estimate from data
#* @param examples the examples
#*/
      estimate(DataSet examples):
        if (examples.getDescription() == null):
            examples.setDescription(new DataSetDescription(examples))
        }
        classRange = examples.getDescription().getLabelDescription().getDiscreteRange()
        tree = new KDTree(examples, distanceMeasure)
    }
    
#/**
#* Get the class distribution
#* @param data the data
#* @return the class distribution
#*/
     Distribution distributionFor(Instance data):
        double[] distribution = new double[classRange]
        Object[] results
        if (range > 0):
            results = tree.knnrange(data, k, range)
        } else {
            results = tree.knn(data, k)
        }
        for (int i = 0 i < results.length i++):
            Instance neighbor = (Instance) results[i]
            if (weightByDistance):
                distribution[neighbor.getLabel().getDiscrete()] +=
                     neighbor.getWeight()/distanceMeasure.value(data, neighbor)
            } else {
                distribution[neighbor.getLabel().getDiscrete()] +=
                     neighbor.getWeight()
            }
        }
        double sum = 0
        for (int i = 0 i < distribution.length i++):
            sum += distribution[i]
        }
        if (Double.isInfinite(sum)):
            sum = 0
            for (int i = 0 i < distribution.length i++):
                if (Double.isInfinite(distribution[i])):
                    distribution[i] = 1
                    sum ++
                } else {
                    distribution[i] = 0
                }
            }
        }
        for (int i = 0 i < distribution.length i++):
            distribution[i] /= sum
        }
        return new DiscreteDistribution(distribution)
    }
    
#/**
#* Get the classification for an example
#* @param data the data to get the classification for
#* @return the classification
#*/
     Instance value(Instance data):
        return distributionFor(data).mode()
    }
    
#/**
#* Get the distance measure
#* @return the distance measure
#*/
     DistanceMeasure getDistanceMeasure():
        return distanceMeasure
    }

#/**
#* Get the k value
#* @return the k value
#*/
     int getK():
        return k
    }

#/**
#* Does it weight by distance
#* @return true if it does
#*/
     boolean isWeightByDistance():
        return weightByDistance
    }

#/**
#* Set the distance measure
#* @param measure the new measure
#*/
      setDistanceMeasure(DistanceMeasure measure):
        distanceMeasure = measure
    }

#/**
#* Set the k value
#* @param i the new k
#*/
      setK(int i):
        k = i
    }

#/**
#* Set the new weighting policy
#* @param b the new policy
#*/
      setWeightByDistance(boolean b):
        weightByDistance = b
    }

}







