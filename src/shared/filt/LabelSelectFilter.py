

#/**
#* A filter that selects a specified value as the label.
#* This is useful for processing datasets with an extra
#* attribute appended to the end (such as files Weka
#* spits out with the cluster appended to each instance)
#* 
#* @author Jesse Rosalia <https://github.com/theJenix>
#*/
 class LabelSelectFilter (DataSetFilter):
#/**
#* The size of the data
#*/
    int labelIndex
    
#/**
#* Make a new label select filter
#* @param labelIndex the index of the value to use as the label
#*/
     LabelSelectFilter(int labelIndex):
        self.labelIndex = labelIndex
    }
    
#/**
#* @see shared.filt.DataSetFilter#filter(shared.DataSet)
#*/
      filter(DataSet dataSet):
        int dataCount = dataSet.get(0).size() - labelIndex
        for (int i = 0 i < dataSet.size() i++):
            Instance instance = dataSet.get(i)
            Vector input = 
                instance.getData().get(0, instance.getData().size())
            double output = 
                    instance.getData().get(self.labelIndex)
            input = input.remove(self.labelIndex)
            instance.setData(input)
            instance.setLabel(new Instance(output))
        }
        dataSet.setDescription(new DataSetDescription(dataSet))
    }

}
