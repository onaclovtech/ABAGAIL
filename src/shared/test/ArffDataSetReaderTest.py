


#/**
#* A data set reader
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class ArffDataSetReaderTest {
#/**
#* The test main
#* @param args ignored parameters
#*/
     static  main(String[] args) throws Exception {
        DataSetReader dsr = new ArffDataSetReader(new File("").getAbsolutePath() + "/src/shared/test/abalone.arff")
        // read in the raw data
        DataSet ds = dsr.read()
        // split out the label
        LabelSplitFilter lsf = new LabelSplitFilter()
        lsf.filter(ds)
        ContinuousToDiscreteFilter ctdf = new ContinuousToDiscreteFilter(10)
        ctdf.filter(ds)
        DataSetLabelBinarySeperator.seperateLabels(ds)
        System.out.println(ds)
        System.out.println(new DataSetDescription(ds))
    }
}
