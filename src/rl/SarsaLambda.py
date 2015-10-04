

#/**
#* An implementation of sarsa lambda
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class SarsaLambda (PolicyLearner):
#/** The zero tolerance */
    static final double ZERO = 1E-6
    
#/**
#* The lambda value
#*/
    double lambda
#/**
#* The decay value
#*/
    double gamma
#/**
#* The alpha value
#*/
    double alpha
#/**
#* How quickly to decay alpha
#*/
    double decay
    
#/**
#* The exploration strategy
#*/
    ExplorationStrategy strategy
#/**
#* The process
#*/
    MarkovDecisionProcess process
#/**
#* The q values
#*/
    double[][] values
#/**
#* The eligibility of each state action
#*/
    double[][] eligibility
#/**
#* The current state
#*/
    int state
#/**
#* The current action
#*/
    int action
#/**
#* The current iteration
#*/
    int iteration
#/**
#* The current episode
#*/
    int episode
#/**
#* The total reward
#*/
    double totalReward
    
#/**
#* Make a new td lambda
#* @param lambda the lambda value
#* @param gamma the gamma value
#* @param alpha the moving average value
#* @param decay the alpha decay value
#* @param process the mdp itself
#*/
     SarsaLambda(double lambda, double gamma, double alpha,
            double decay, ExplorationStrategy strategy,  MarkovDecisionProcess process):        
        self.lambda = lambda
        self.gamma = gamma
        self.alpha = alpha
        self.decay = decay
        self.strategy = strategy
        self.process = process
        
        self.values = new double[process.getStateCount()][process.getActionCount()]
        self.eligibility = new double[process.getStateCount()][process.getActionCount()]
        self.state = process.sampleInitialState()
        self.action = Distribution.random.nextInt(process.getActionCount())
    }

#/**
#* @see shared.Trainer#train()
#*/
     double train():
        int nextState = process.sampleState(state, action)
        double reward = process.reward(nextState, action)
        totalReward += reward
        int nextAction = strategy.action(values[nextState])
        // calculate the value change
        double delta = reward + gamma * values[nextState][nextAction]
            - values[state][action]
        // pump the eligibility for self tate
        eligibility[state][action] += 1
        double difference = 0
        // update all state acion pairs
        for (int i = 0 i < process.getStateCount() i++):
            for (int a = 0 a < process.getActionCount() a++):
                if (eligibility[i][a] < ZERO):
                    continue
                }
                // calculate the change in values
                double newValue = values[i][a] + alpha * delta * eligibility[i][a]
                difference = Math.max(difference, Math.abs(values[i][a] - newValue))
                values[i][a] = newValue
                eligibility[i][a] *= gamma * lambda
            }
        }
        state = nextState
        action = nextAction
        // reset on terminal state
        if (process.isTerminalState(state)):
            episode++
            state = process.sampleInitialState()
            action = strategy.action(values[state])
            for (int i = 0 i < process.getStateCount() i++):
                for (int a = 0 a < process.getActionCount() a++):
                    eligibility[i][a] = 0
                }
            }
        }
        iteration++
        // decay the alpha value
        alpha *= decay
        return difference
    }
    

#/**
#* @see rl.PolicyLearner#getPolicy()
#*/
     Policy getPolicy():
        int stateCount = process.getStateCount()
        int actionCount = process.getActionCount()
        // calculate the policy based on the values
        int[] policy = new int[stateCount]
        for (int i = 0 i < stateCount i++):
            // find the maximum action
            double maxActionVal = 0
            int maxAction = 0
            for (int a = 0 a < actionCount a++):
                double actionVal = values[i][a]
                if (actionVal > maxActionVal):
                    maxActionVal = actionVal
                    maxAction = a
                }
            }
            policy[i] = maxAction
        }
        return new Policy(policy)
    }
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return iteration + ", " + episode
    }
#/**
#* Get the totalReward
#* @return returns the totalReward
#*/
     double getTotalReward():
        return totalReward
    }
}
