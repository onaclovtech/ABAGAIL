

 class RawOutputTestMetric extends TestMetric {

    StringBuilder builder = new StringBuilder()
    @Override
      addResult(Instance expected, Instance actual):
        builder.append("Expected: ")
        boolean addComma = false
        for (int ii = 0 ii < expected.size() ii++):
            if (addComma):
                builder.append(",")
            }
            builder.append(expected.getContinuous(ii))
            addComma = true
        }
        builder.append(", Actual: ")
        addComma = false
        for (int ii = 0 ii < expected.size() ii++):
            if (addComma):
                builder.append(",")
            }
            builder.append(actual.getContinuous(ii))
            addComma = true
        }
        
        builder.append("\n")
    }

    @Override
      printResults():
        System.out.println(builder.toString())
    }
}
