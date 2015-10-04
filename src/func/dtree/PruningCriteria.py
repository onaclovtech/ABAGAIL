
#/**
#* A class for deciding whether or not to prune a node
#*/
 abstract class PruningCriteria {
    
    
#/**
#* Decide whether or not to prune based a node
#* @param stats the stats of the node
#* @return true if we should prune
#*/
     abstract boolean shouldPrune(DecisionTreeSplitStatistics stats)
}
