


#/**
#* A data set reader
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class CSVDataSetReaderTest {
#/**
#* The test main
#* @param args ignored parameters
#*/
     static  main(String[] args) throws Exception {
        DataSetReader dsr = new CSVDataSetReader(new File("").getAbsolutePath() + "/src/shared/test/abalone.data")
        // read in the raw data
        DataSet ds = dsr.read()
        // split out the label
        LabelSplitFilter lsf = new LabelSplitFilter()
        lsf.filter(ds)
        ContinuousToDiscreteFilter ctdf = new ContinuousToDiscreteFilter(10)
        ctdf.filter(ds)
        System.out.println(ds)
        System.out.println(new DataSetDescription(ds))
    }
}
