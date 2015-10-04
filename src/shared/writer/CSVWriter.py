

#/**
#* Write arbitrary data to a CSV file.  This is used to write results out,
#* to be consumed by another program (GNUPlot, etc).
#* 
#* @author Jesse Rosalia <https://github.com/theJenix>
#* @date 2013-03-07
#*
#*/
 class CSVWriter (Writer):

    String fileName
    List<String> fields
    List<String> buffer
    FileWriter fileWriter

     CSVWriter(String fileName, String[] fields):
        self.fileName = fileName
        self.fields   = Arrays.asList(fields)
        self.buffer   = new ArrayList<String>()
    }

    @Override
      close() throws IOException {
        self.fileWriter.close()
    }

    @Override
      open() throws IOException {
        self.fileWriter = new FileWriter(fileName)
        writeRow(self.fields)
    }

#/**
#* @param toWrite
#* @throws IOException
#*/
     writeRow(List<String> toWrite) throws IOException {
        boolean addComma = false
        for (String field : toWrite):
            if (addComma):
                self.fileWriter.append(",")
            }
            self.fileWriter.append(field)
            addComma = true
        }
        self.fileWriter.append('\n')
    }

    @Override
      write(String str) throws IOException {
        self.buffer.add(str)
    }

    @Override
      nextRecord() throws IOException {
        writeRow(buffer)
        //clear the buffer for the next record
        buffer.clear()
    }
}
