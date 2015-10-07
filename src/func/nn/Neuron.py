#/**
# * A node in a neural network implementation
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class Neuron:
   
#   /**
#    * Make a new node
#    */
   def __init__(self):
      self.inLinks = []
      self.outLinks = []
      self.activation = 0.0

#   /**
#    * Get the error value
#    * @return the error
#    */
   def getActivation(self):
      return self.activation
   
#   /**
#    * Set the value
#    * @param value the new value
#    */
   def setActivation(self, value):
      self.activation = value

#   /**
#    * Get the input links
#    * @return the list of links
#    */
   def getInLinks(self):
      return self.inLinks
   
#   /**
#    * Get the number of in links
#    * @return the number of in links
#    */
   def getInLinkCount(self):
      return len(self.inLinks)
   
#   /**
#    * Get in link number i
#    * @param i the in link index
#    * @return the link
#    */
   def getInLink(self, i):
      return self.inLinks[i]

#   /**
#    * Get the output links
#    * @return the output links
#    */
   def getOutLinks(self):
      return self.outLinks

#   /**
#    * Add a in link
#    * @param link the link to add
#    */
   def addInLink(self, link):
      self.inLinks.append(link)

#   /**
#    * Add a out link
#    * @param link the link to add
#    */
   def addOutLink(self, link):
      self.outLinks.append(link)

#   /**
#    * Get the number of out links
#    * @return the number of out links
#    */
   def getOutLinkCount(self):
      return self.outLinks.size()
   
#   /**
#    * Get out link number i
#    * @param i the out link index
#    * @return the link
#    */
   def getOutLink(self, i):
      return self.outLinks.get(i)
   
#   /**
#    * Remove the given in link
#    * @param link the link to remove
#    */
   def removeInLink(self, link):
      self.inLinks.remove(link)
   
#   /**
#    * Remove the given out link
#    * @param link the link to remove
#    */
   def removeOutLink(self, link):
      self.outLinks.remove(link)

#   /**
#    * Create a new link
#    * @return the link to use
#    */
   def createLink(self):
      return Link()
   
#   /**
#    * Connect this node to the given node
#    * @param node the node to connect to
#    */
   def connect(self, node):
      link = self.createLink()
      link.setInNode(self)
      link.setOutNode(node)     
      self.addOutLink(link)
      node.addInLink(link)

#   /**
#    * Disconnect this node from the given node
#    * @param node the node to disconnect from
#    */
   def disconnect(self, node):
      for i in range(len(self.outLinks())):
         link = outLinks.get(i)
         if (link.getInNode() == this):
            outLinks.remove(link)
            break
      for i in range(len(node.getInLinks())):
         link = node.getInLinks().get(i)
         if (link.getInNode() == this):
            node.removeInLink(link)
            break
