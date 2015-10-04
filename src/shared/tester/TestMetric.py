

#/**
#* This interface defines an API for test metrics.  Test metrics are notified by the Tester
#* after an instance is tested by the classifier.  The test metrics are given a chance to compare
#* the results and accumulate statics or measurements of error.  These data can then be printed
#* in a human readable format.
#* 
#* @author Jesse Rosalia (https://www.github.com/theJenix)
#* @date 2013-03-05
#*/
 abstract class TestMetric {

#/**
#* Add a test result to the metric.  The metric will compare the values and
#* accumulate what data it needs.
#* 
#* @param expected The expected value (from the training set)
#* @param actual The value produced by the classifier.
#*/
     abstract  addResult(Instance expected, Instance actual)

#/**
#* Bulk add a test results to the metric.  The metric will compare the values and
#* accumulate what data it needs.
#* 
#* @param expected The expected values from the training set.
#* @param actual The values produced by the classifier.
#*/
      addResult(DataSet expected, DataSet actual):
        // Sanity check sizes.
        if (expected.size() != actual.size()):
            throw new RuntimeException("Something is wrong. "
                    + "Expected data set and actual data set sizes are not the same.")
        }
        for (int i = 0 i < expected.size() i++):
            self.addResult(expected.get(i), actual.get(i))
        }
    }

#/**
#* Print the values collected by self test metric.
#* 
#*/
     abstract  printResults()
}
