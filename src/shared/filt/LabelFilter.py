

#/**
#* A filter that applies a filter to the label data set
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class LabelFilter (ReversibleFilter):
#/**
#* The filter to apply
#*/
    DataSetFilter filter

#/**
#* @see shared.filt.DataSetFilter#filter(shared.DataSet)
#*/
      filter(DataSet dataSet):
        filter.filter(dataSet.getLabelDataSet())
    }

#/**
#* @see shared.filt.ReversibleFilter#reverse(shared.DataSet)
#*/
      reverse(DataSet set):
        ((ReversibleFilter) filter).reverse(set.getLabelDataSet())
    }

}
