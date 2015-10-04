

#/**
#* Class to read in data from a CSV file without a specified label
#* @author Tim Swihart <https://github.com/chronoslynx>
#* @date 2013-03-05
#*/
 class CSVDataSetReader extends DataSetReader {

	 CSVDataSetReader(String file):
		super(file)
		// TODO Auto-generated constructor stub
	}

	@Override
	 DataSet read() throws Exception {
        BufferedReader br = new BufferedReader(new FileReader(file))
        String line
        List<Instance> data = new ArrayList<Instance>()
        Pattern pattern = Pattern.compile("[ ,]+")
        while ((line = br.readLine()) != null):
            String[] split = pattern.split(line.trim())
            double[] input = new double[split.length]
            for (int i = 0 i < input.length i++):
                input[i] = Double.parseDouble(split[i])
            }
            Instance instance = new Instance(input)
            data.add(instance)
        }
        br.close()
        Instance[] instances = (Instance[]) data.toArray(new Instance[0])
        DataSet set = new DataSet(instances)
        set.setDescription(new DataSetDescription(set))
        return set
	}

}
