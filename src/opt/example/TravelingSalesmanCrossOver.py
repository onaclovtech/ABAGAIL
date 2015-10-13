import random
from src.opt.example.TravelingSalesmanEvaluationFunction import *
from src.shared.Instance import *
#/**
#* A cross over function for a traveling`
#* salesman problem, based on
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class TravelingSalesmanCrossOver:
    
#/**
#* The evaluation function
#*/
    #TravelingSalesmanEvaluationFunction eval
    
#/**
#* Make a new traveling salesman cross over
#* @param eval the evaluation function to use
#*/
     def __init__(self,eval):
        if not isinstance(eval, TravelingSalesmanEvaluationFunction):
            raise TypeError("Expected TravelingSalesmanEvaluationFunction got " + str(eval.__class__))
        self.eval = eval
    

#/**
#* @see opt.ga.CrossOverFunction#mate(opt.OptimizationData, opt.OptimizationData)
#*/
     def mate(self, a, b):
        if not isinstance(a, Instance):
            raise TypeError("Expected Instance got " + str(a.__class__))
        if not isinstance(b, Instance):
            raise TypeError("Expected Instance got " + str(b.__class__))
        nexta = [None] * a.size()
        nextb = [None] * b.size()
        for i in range(a.size()-1):
            nexta[a.getDiscrete(i)] = a.getDiscrete(i+1)
            nextb[b.getDiscrete(i)] = b.getDiscrete(i+1)
        
        nexta[a.getDiscrete(a.size() - 1)] = a.getDiscrete(0)
        nexta[b.getDiscrete(b.size() - 1)] = b.getDiscrete(0)
        visited = [None] * a.size()
        child = [None] * a.size()
        child[0] = random.randint(0,a.size())
        visited[child[0]] = True
        for i in range(len(child)-1): #Is -1 necessary?
            cur = child[i]
            na = nexta[cur]
            nb = nextb[cur]
            next = -1
            if (not visited[na] is None and visited[nb] is None):
                next = nb
            elif (visited[nb] and not visited[na]):
                   next = na
            elif (not visited[na] and not visited[nb]):
                if (self.eval.getDistance(cur, na) < self.eval.getDistance(cur, nb)):
                    next = na
                else:
                    next = nb
            else:
                while True: 
                    next = random.randint(0,a.size()-1)
                    if visited[next]:
                        break
            child[i+1] = next
            visited[next] = True
        
        # Not sure what hte point of below is, you could just return Instance ds = child....strange
        data = [None] * len(child)
        
        for i in range(len(child)):
            data[i] = child[i]
        
        return Instance(ds = data)
    
