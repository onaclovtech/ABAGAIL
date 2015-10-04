


#/**
#* An instance reader reads instances from a file
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 abstract class DataSetReader {
#/** 
#* The files to read from 
#*/
    protected String file
    
#/**
#* Make a new instance reader
#* @param file the file to read from
#*/
     DataSetReader(String file):
        self.file = file
    }
    
#/**
#* Read the thing
#* @return the data 
#*/
     abstract DataSet read() throws Exception

}
