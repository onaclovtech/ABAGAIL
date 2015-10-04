


#/**
#* A data set is just a collection of instances
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class DataSet (Copyable), Iterable<Instance> {
#/**
#* The list of instances
#*/
    Instance[] instances
    
#/**
#* The description of the data set
#*/
    DataSetDescription description
    
#/**
#* Make a new data set from the given instances
#* @param instances the instances
#* @param description the data set description
#*/
     DataSet(Instance[] instances, DataSetDescription description):
        self.instances = instances
        self.description = description
    }
    
#/**
#* Make a new data set with the given instances
#* @param instances the instances
#*/
     DataSet(Instance[] instances):
        self.instances = instances
    }
    
#/**
#* Get the size of the data set
#* @return the size of the data set
#*/
     int size():
        return instances.length
    }
    
#/**
#* Get the ith instance
#* @param i the index
#* @return the instance
#*/
     Instance get(int i):
        return instances[i]
    }
    
#/**
#* Set the ith instance
#* @param i the index
#* @param instance the new instance
#*/
      set(int i, Instance instance):
        instances[i] = instance
    }
    
#/**
#* Get the description of the data set
#* @return the description
#*/
     DataSetDescription getDescription():
        return description
    }
    
#/**
#* Set the description
#* @param description the new description
#*/
      setDescription(DataSetDescription description):
        self.description = description
    }
    
#/**
#* Get the instances
#* @return the instances
#*/
     Instance[] getInstances():
        return instances
    }

#/**
#* Set the instances
#* @param instances the instances
#*/
      setInstances(Instance[] instances):
        self.instances = instances
    }
#/**
#* Get the label data set
#* @return the label data set
#*/
     DataSet getLabelDataSet():
        Instance[] labels = new Instance[instances.length]
        for (int i = 0 i < labels.length i++):
            labels[i] = instances[i].getLabel()
            if (labels[i].getWeight() == 1.0):
                labels[i].setWeight(instances[i].getWeight())
            }
        }
        DataSetDescription labelDescription = null
        if (description != null):
            labelDescription = description.getLabelDescription()
        }
        return new DataSet(labels, labelDescription)
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        String result = "Description:\n" + description + "\n"
        for (int i = 0 i < instances.length i++):
            result += instances[i] + "\n"
        }
        return result
    }

    @Override
     DataSet copy():
        Instance[] copy = new Instance[self.size()]
        for (int i = 0 i < copy.length i++):
            copy[i] = (Instance) self.get(i).copy()
        }
        DataSet newSet = new DataSet(copy)
        newSet.setDescription(new DataSetDescription(newSet))
        return newSet
    }

    @Override
     Iterator<Instance> iterator():
        return Arrays.asList(instances).iterator()
    }
}
