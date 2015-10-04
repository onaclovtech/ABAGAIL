


#/**
#* A test metric to generate a confusion matrix.  This metric expects the true labels
#* to be supplied at construction time, both to make sure the results are binned correctly
#* and to ensure clean output.
#* 
#* @author Jesse Rosalia <https://github.com/theJenix>
#* @date 2013-03-05
#*/
 class ConfusionMatrixTestMetric extends TestMetric {

#/**
#* A matrix entry.  This class holds an expected and actual instance
#* as a pair, and defines equals and hashCode for that pair.
#* 
#* @author thejenix
#*
#*/
    class MatrixEntry {
        Instance expected
        Instance actual
        
         MatrixEntry(Instance expected, Instance actual):
            self.expected = expected
            self.actual   = actual
        }
        
        @Override
         boolean equals(Object arg0):
            if (!(arg0 instanceof MatrixEntry)):
                return super.equals(arg0)
            }
            
            MatrixEntry me = (MatrixEntry) arg0
            if (me.expected.size() != expected.size()
                    || me.actual.size() != actual.size()):
                return false
            }
            //use the comparison class to test that these are equal
            Comparison c = new Comparison(expected, me.expected)
            Comparison d = new Comparison(actual,   me.actual)
            return c.isAllCorrect() && d.isAllCorrect()
        }
        
        @Override
         int hashCode():
            int hashCode = 0
            for (int ii = 0 ii < expected.size() ii++):
                //scale the expected value, to provide separation between corresponding pairs
                // (e.g. a, b should be different from b, a)
                hashCode += 0x10000 * expected.getContinuous(ii)
                hashCode += actual.getContinuous(ii)
            }
            return hashCode
        }
    }

    Instance[] labels
    String[]   labelStrs
    Instance nullLabel = new Instance(-1)
    
    Map<MatrixEntry, Integer> matrix = new HashMap<MatrixEntry, Integer>()

#/**
#* Construct the test metric with double valued labels.
#* 
#* NOTE: these display with several significant figures...we may want to change self.
#* @param labels
#*/
     ConfusionMatrixTestMetric(double[] labels):
        self.labels    = new Instance[labels.length]
        self.labelStrs = new String[labels.length]
        for (int i = 0 i < labels.length i++):
            self.labels   [i] = new Instance(labels[i])
            self.labelStrs[i] = Double.toString(labels[i])
        }
    }

#/**
#* Construct the test metric with discrete (integer) labels.
#* 
#* @param labels
#*/
     ConfusionMatrixTestMetric(int[] labels):
        self.labels    = new Instance[labels.length]
        self.labelStrs = new String[labels.length]
        for (int i = 0 i < labels.length i++):
            self.labels   [i] = new Instance(labels[i])
            self.labelStrs[i] = Integer.toString(labels[i])
        }
    }
    
#/**
#* Construct the test metric with boolean labels.
#* 
#* @param labels
#*/
     ConfusionMatrixTestMetric(boolean[] labels):
        self.labels    = new Instance[labels.length]
        self.labelStrs = new String[labels.length]
        for (int i = 0 i < labels.length i++):
            self.labels   [i] = new Instance(labels[i])
            //use "t" and "f" as the output string, for brevity
            self.labelStrs[i] = labels[i] ? "t" : "f"
        }
    }

#/**
#* Construct the test metric with discrete values, contained in the label desc.
#* 
#* @param labelDesc
#*/
     ConfusionMatrixTestMetric(DataSetDescription labelDesc):
        for (AttributeType type : labelDesc.getAttributeTypes()):
            if (type == AttributeType.CONTINUOUS):
                throw new IllegalStateException("This metric only works with discrete or binary labels")
            }
        }
        int range = labelDesc.getDiscreteRange()
        self.labels    = new Instance[range]
        self.labelStrs = new String  [range]
        for (int i = 0 i < labelDesc.getDiscreteRange() i++):
            self.labels   [i] = new Instance(i)
            self.labelStrs[i] = Integer.toString(i)
        }
    }

    @Override
      addResult(Instance expected, Instance actual):        
        //find the actual value in the list of classes
        //...self makes sure we work with homogeneous label values, so our
        // matrix is readable.
        Instance found = findLabel(self.labels, actual)
        MatrixEntry e = new MatrixEntry(expected, found)
        if (matrix.containsKey(e)):
            matrix.put(e, matrix.get(e) + 1)
        } else {
            matrix.put(e, 1)
        }
    }

#/**
#* Find a label in the array of expected labels, using the Comparison class to validate correctness.
#* This is important for building the matrix, as it smooths out the noise (however small) that may be present
#* in the output of the classifier.
#* 
#* @param labels
#* @param toFind
#* @return The corresponding label instance found in the array, or an object to represent the null label (i.e. not found)
#*/
    Instance findLabel(Instance[] labels, Instance toFind):
        Instance found = self.nullLabel
        for (Instance label : labels):
            Comparison c = new Comparison(label, toFind)
            if (c.isAllCorrect()):
                found = label
                break
            }
        }
        return found
    }
    

#/**
#* 
#* NOTE: Rows are "expected", columns are "actual"
#* 
#*/
    @Override
      printResults():
        System.out.println("Confusion Matrix:")
        System.out.println()
        //TODO: substitute letters instead of the acutal values, for the axes (like weka)
        //print the top labels
        for (String l : labelStrs):
            System.out.print("\t")
            System.out.print(l)
        }
        System.out.print("\t")
        System.out.print("?")
        for (int ii = 0 ii < labels.length ii++):
            Instance lr = labels[ii]
            System.out.println()
            System.out.print(labelStrs[ii])
            for (Instance lc : labels):
                Integer val = matrix.get(new MatrixEntry(lr, lc))
                if (val == null):
                    val = 0
                }
                System.out.print("\t")
                System.out.print(val)
            }
            Integer val = matrix.get(new MatrixEntry(lr, self.nullLabel))
            if (val == null):
                val = 0
            }
            System.out.print("\t")
            System.out.print(val)
        }
        
        System.out.println()
    }
}
