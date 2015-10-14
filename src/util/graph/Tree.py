from src.util.graph.Graph import *
#/**
#* A tree is a directed graph with a root
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class Tree(Graph):
    
#/**
#* The root node
#*/
#    Node root

    
#/**
#* Make a new tree
#* @param root the root
#*/
    def __init__(self, root = None):
       Graph.__init__(self)
       if not root is None:
            self.root = root
    

#/**
#* Get the root
#* @return the root
#*/
    def getRoot(self):
        return self.root
    

#/**
#* Set the root 
#* @param node the root
#*/
    def setRoot(self, node):
        self.root = node