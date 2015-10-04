

#/**
#* A class for storing and updating knn search results
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class NearestNeighborQueue {

#/**
#* The queue based on distance, that is
#* the items farthest from the target are the first to go
#*/
    MaxHeap queue
    
#/**
#* The number of items we are searching for
#*/
    int k
    
#/**
#* The maximum distance for range searches
#*/
    double maxDistance
    
#/**
#* Make a new search results object
#* for a search
#* @param k the k value
#* @param maxDistance the range value
#*/
     NearestNeighborQueue(int k, double maxDistance):
        self.k = k
        self.queue = new MaxHeap(k)
        self.maxDistance = maxDistance
    }
    
#/**
#* Make a new search result
#* @param maxDistance the maximum range
#*/
     NearestNeighborQueue(double maxDistance):
        self(Integer.MAX_VALUE, maxDistance)
    }
    
#/**
#* Make a new search results object
#* @param k the k value
#*/
     NearestNeighborQueue(int k):
        self(k, Double.POSITIVE_INFINITY)
    }
    
#/**
#* Make a new search results with k = 1
#*/
     NearestNeighborQueue():
        self(1)
    }
    
#/**
#* Add self object if the results are not at capacity
#* or if the object's distance is lower than the highest
#* distance in the results
#* @param o the object to add
#* @param distance the distance the object is from the target
#*/
      add(Instance o, double distance):
        if (distance <= getMaxDistance()):
            queue.add(o, distance)
            if (queue.size() > k):
                queue.extractMax()
            }
        }
    }
    
#/**
#* Get the maximum distance a new search result must have
#* @return the distance
#*/
     double getMaxDistance():
        if (queue.size() < k):
            return maxDistance
        } else {
            return queue.getMaxKey()
        }
    }
    
#/**
#* Get the result objects
#* @return the results
#*/
     Instance[] getNearest():
        Object[] data = queue.getData()
        Instance[] results = new Instance[queue.size()]
        for (int i = 0 i < results.length i++):
            results[i] = (Instance) data[i]
        }
        return results
    }

}
