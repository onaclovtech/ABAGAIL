

#/**
#* A class for writing data sets
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class DataSetWriter {
#/**
#* The dat set
#*/
    DataSet set
    
#/**
#* The file name
#*/
    String filename

#/**
#* True to append the results to the end of
#*  the file, false to overwrite.  This is
#*  useful if we need to write some kind of
#*  header to the file before writing the
#*  dataset.
#* 
#*/
    boolean append

    String[] labelStrings

#/**
#* Make a new data set writer
#* @param set the data set to writer
#*/
     DataSetWriter(DataSet set, String filename):
        self.set = set
        self.filename = filename
        self.append = false
        self.labelStrings = null
    }
    
#/**
#* Make a new data set writer
#* @param set the data set to writer
#*/
     DataSetWriter(DataSet set, String filename, boolean append):
        self.set = set
        self.filename = filename
        self.append = append
        self.labelStrings = null
    }

#/**
#* Make a new data set writer
#* @param set the data set to writer
#*/
     DataSetWriter(DataSet set, String filename, boolean append, String[] labelStrings):
        self.set = set
        self.filename = filename
        self.append = append
        self.labelStrings = labelStrings
    }

#/**
#* Write the file out
#* @throws IOException when something goes bad
#*/
      write() throws IOException {
        PrintWriter pw = new PrintWriter(new FileWriter(filename, self.append))
        for (int i = 0 i < set.size() i++):
            Instance data = set.get(i)
            boolean label = false
            while (data != null):
                if (label && self.labelStrings != null):
                    for (int j = 0 j < data.size() j++):
                        pw.print(self.labelStrings[data.getDiscrete(j)])
                        if (j + 1 < data.size() || data.getLabel() != null):
                            pw.print(", ")
                        }
                    }
                } else {
                    for (int j = 0 j < data.size() j++):
                        pw.print(data.getContinuous(j))
                        if (j + 1 < data.size() || data.getLabel() != null):
                            pw.print(", ")
                        }
                    }
                }
                data = data.getLabel()
                label = true
            }
            pw.println()
        }
        pw.close()
    }
}
