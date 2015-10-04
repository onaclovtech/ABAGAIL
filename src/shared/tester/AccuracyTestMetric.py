

#/**
#* A test metric for accuracy.  This metric reports of % correct and % incorrect for a test run.
#* 
#* @author Jesse Rosalia <https://github.com/theJenix>
#* @date 2013-03-05
#*/
 class AccuracyTestMetric extends TestMetric {

    int count    
    int countCorrect
    
    @Override
      addResult(Instance expected, Instance actual):
        Comparison c = new Comparison(expected, actual)

        count++
        if (c.isAllCorrect()):
            countCorrect++
        }
    }
    
     double getPctCorrect():
        return count > 0 ? ((double)countCorrect)/count : 1 //if count is 0, we consider it all correct
    }

      printResults():
        //only report results if there were any results to report.
        if (count > 0):
            double pctCorrect = getPctCorrect()
            double pctIncorrect = (1 - pctCorrect)
            System.out.println(String.format("Correctly Classified Instances: %.02f%%",   100 * pctCorrect))
            System.out.println(String.format("Incorrectly Classified Instances: %.02f%%", 100 * pctIncorrect))
        } else {

            System.out.println("No results added.")
        }
    }
}
