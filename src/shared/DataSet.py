#/**
#* A data set is just a collection of instances
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class DataSet:
#/**
#* The list of instances
#*/
    #Instance[] instances
    
#/**
#* The description of the data set
#*/
    #DataSetDescription description
    
#/**
#* Make a data set from the given instances
#* @param instances the instances
#* @param description the data set description
#*/
     def __init__(self, instances, description = None):
        self.instances = instances
        self.description = description
    
#/**
#* Get the size of the data set
#* @return the size of the data set
#*/
     def size(self):
        return len(self.instances)
    
    
#/**
#* Get the ith instance
#* @param i the index
#* @return the instance
#*/
     def get(self,  i):
        return self.instances[i]
    
    
#/**
#* Set the ith instance
#* @param i the index
#* @param instance the instance
#*/
     def set(self, i, instance):
        self.instances[i] = instance
    
#/**
#* Get the description of the data set
#* @return the description
#*/
     def getDescription(self):
        return self.description
    
#/**
#* Set the description
#* @param description the description
#*/
     def setDescription(self, description):
        self.description = description
      
#/**
#* Get the instances
#* @return the instances
#*/
     def getInstances(self):
        return self.instances
    

#/**
#* Set the instances
#* @param instances the instances
#*/
     def setInstances(self, instances):
        self.instances = instances
    
#/**
#* Get the label data set
#* @return the label data set
#*/
     def getLabelDataSet(self):
        labels = Instance[instances.length]
        for i in range(len(labels)):
            labels[i] = instances[i].getLabel()
            if (labels[i].getWeight() == 1.0):
                labels[i].setWeight(instances[i].getWeight())
            
        
        labelDescription = null
        if (description != null):
            labelDescription = description.getLabelDescription()
        
        return DataSet(labels, labelDescription)
    
    
#/**
#* @see java.lang.Object#toString()
#*/
     def toString(self):
        result = "Description:\n" + description + "\n"
        for i in range(len(self.instances)):
            result += instances[i] + "\n"
        
        return result
    

    #@Override
     def copy(self):
        copy = Instance[self.size()]
        for i in range(len(copy)):
            copy[i] = self.get(i).copy()
        
        newSet = DataSet(copy)
        newSet.setDescription(DataSetDescription(newSet))
        return newSet
    

   # @Override
#     Iterator<Instance> iterator():
#        return Arrays.asList(instances).iterator()
