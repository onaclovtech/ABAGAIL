
#/**
#* A tree is a directed graph with a root
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class Tree extends Graph {
    
#/**
#* The root node
#*/
    Node root
    
#/**
#* Make a rooted graph
#*/
     Tree():
    }
    
#/**
#* Make a new tree
#* @param root the root
#*/
     Tree(Node root):
        self.root = root
    }

#/**
#* Get the root
#* @return the root
#*/
     Node getRoot():
        return root
    }

#/**
#* Set the root 
#* @param node the root
#*/
      setRoot(Node node):
        root = node
    }

}
