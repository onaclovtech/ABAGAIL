

#/**
#* A K means clusterer
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class KMeansClusterer extends AbstractConditionalDistribution (FunctionApproximater):
#/**
#* The cluster centers
#*/
    Instance[] clusterCenters
    
#/**
#* The number of clusters
#*/
    int k
    
#/**
#* The distance measure
#*/
    DistanceMeasure distanceMeasure
    
#/**
#* Make a new k means clustere
#* @param k the k value
#* @param distanceMeasure the distance measure
#*/
     KMeansClusterer(int k):
        self.k = k
        self.distanceMeasure = new EuclideanDistance()
    }
    
#/**
#* Make a new clusterer
#*/
     KMeansClusterer():
        self(2)
    }

#/**
#* @see func.Classifier#classDistribution(shared.Instance)
#*/
     Distribution distributionFor(Instance instance):
        double[] distribution = new double[k]
        for (int i = 0 i < k i++):
            distribution[i] +=
                1/distanceMeasure.value(instance, clusterCenters[i])   
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
#* @see func.FunctionApproximater#estimate(shared.DataSet)
#*/
      estimate(DataSet set):
        clusterCenters = new Instance[k]
        int[] assignments = new int[set.size()]
        // random initial centers
        for (int i = 0 i < clusterCenters.length i++):
            int pick
            do {
                pick = Distribution.random.nextInt(set.size())
            } while (assignments[pick] != 0)
            assignments[pick] = 1
            clusterCenters[i] = (Instance) set.get(pick).copy()
        }
        boolean changed = false
        // the main loop
        do {
            changed = false
            // make the assignments
            for (int i = 0 i < set.size() i++):
                // find the closest center
                int closest = 0
                double closestDistance = distanceMeasure
                    .value(set.get(i), clusterCenters[0])
                for (int j = 1 j < k j++):
                    double distance = distanceMeasure
                        .value(set.get(i), clusterCenters[j])
                    if (distance < closestDistance):
                        closestDistance = distance
                        closest = j
                    }
                }
                if (assignments[i] != closest):
                    changed = true
                }
                assignments[i] = closest
            }
            if (changed):
                double[] assignmentCount = new double[k]
                // make the new clusters
                for (int i = 0 i < k i++):
                    clusterCenters[i].setData(new DenseVector(
                        clusterCenters[i].getData().size()))
                }
                for (int i = 0 i < set.size() i++):
                    clusterCenters[assignments[i]].getData().plusEquals(
                        set.get(i).getData().times(set.get(i).getWeight()))
                    assignmentCount[assignments[i]] += set.get(i).getWeight()    
                }
                for (int i = 0 i < k i++):
                    clusterCenters[i].getData().timesEquals(1/assignmentCount[i])
                }
            }
        } while (changed)
    }

#/**
#* @see func.FunctionApproximater#value(shared.Instance)
#*/
     Instance value(Instance data):
        return distributionFor(data).mode()
    }

#/**
#* Get the cluster centers
#* @return the cluster centers
#*/
     Instance[] getClusterCenters():
        return clusterCenters
    }
        
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        String result = "k = " + k + "\n"
        for (int i = 0 i < clusterCenters.length i++):
            result += clusterCenters[i].toString() + "\n"
        }
        return result
    }


}
