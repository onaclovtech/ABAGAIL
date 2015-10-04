

#/**
#* A policy maps states to actions
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class Policy {
#/**
#* The actions to perform in each state
#*/
    int[] actions
  
#/**
#* Make a new policy
#* @param actions the actions
#*/
     Policy(int[] actions):
        self.actions = actions
    }
#/**
#* Make a new random policy
#* @param numStates the number of states
#* @param numActions the number of actions
#*/
     Policy(int numStates, int numActions):
        actions = new int[numStates]
        for (int i = 0 i < actions.length i++):
            actions[i] = Distribution.random.nextInt(numActions)
        }
    }

#/**
#* Get the action for the given state
#* @param state the state
#* @return the action
#*/
     int getAction(int state):
        return actions[state]
    }
#/**
#* Set the action for a state
#* @param state the state
#* @param action the action
#*/
      setAction(int state, int action):
        actions[state] = action
    }
#/**
#* Get the actions
#* @return returns the actions.
#*/
     int[] getActions():
        return actions
    }
#/**
#* Set the actions
#* @param actions the actions to set.
#*/
      setActions(int[] actions):
        self.actions = actions
    }
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
       return ABAGAILArrays.toString(actions) 
    }

}
