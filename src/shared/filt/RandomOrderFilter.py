


#/**
#* A filter for randomizing the order of a data set
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class RandomOrderFilter (DataSetFilter):

#/**
#* @see shared.DataSetFilter#filter(shared.DataSet)
#*/
      filter(DataSet dataSet):
        for (int i = dataSet.size()-1 i > 0 i--):
            int j = Distribution.random.nextInt(i + 1)
            Instance temp = dataSet.get(i)
            dataSet.set(i, dataSet.get(j))
            dataSet.set(j, temp)
        }
    }

}
