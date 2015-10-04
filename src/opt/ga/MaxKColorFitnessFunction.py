#/**
# * A Max K Color evaluation function
# * @author kmandal
# * @version 1.0
# */
class MaxKColorFitnessFunction(EvaluationFunction):
    
    def __init__(Vertex[] vertices):
        self.vertices = vertices
        self.graphSize = vertices.length
        self.conflict = false
        
#    /**
#     * @see opt.EvaluationFunction#value(opt.OptimizationData)
#     * Find how many iterations does it take to find if k-colors can be or can not be assigned to a given graph.
#     */
    def value(self, Instance d):
        Vector data = d.getData()
        int n = data.size()
        double iterations = 0
        self.conflict = false
        for (int i = 0; i < n-1; i++):
            int sampleColor = ((int) data.get(i))
            for(int j = 0; j < self.graphSize; j++):
              Vertex vertex = self.vertices[j]
              iterations ++
              if(vertex.getAadjacencyColorMatrix().contains(sampleColor)):
            	  // if any of the adjacent vertices contains the color, the color can't be assigned to this vertex
            	  self.conflict = true
            	  break
        return iterations
    
    def foundConflict(self):
    	return self.conflict ? "Failed to find Max-K Color combination !" : "Found Max-K Color Combination !"
