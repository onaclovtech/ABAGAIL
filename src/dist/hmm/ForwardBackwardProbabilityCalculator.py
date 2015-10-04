

#/**
#* An implementation of the forward backward algorithm,
#* which computes forward and backward probabilities
#* for use in the Viterbi and Baum-Welch algorithms
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class ForwardBackwardProbabilityCalculator {

#/**
#* The forward probabilities through time, 
#* that is [t][i] value of in self matrix is the
#* probability of being in state i at time t and
#* O_1, O_2, ... O_t.  These are the alpha values
#* in the classic Rabiner paper
#*/
    double[][] forwardProbabilities

#/**
#* The backward probabilities through time,
#* that is the [t][i] value in self matrix is the
#* probability of O_t+1, O_t+2, ... O_T given
#* that the state is i at time t.  These are the
#* beta values in the classic Rabiner paper.
#*/
    double[][] backwardProbabilities
    
#/**
#* The array of scaling values used to keep the
#* probabilities within the dynamic range of
#* the computer
#*/
    double[] scales

#/**
#* The model used to calculate the probabilities
#*/
    HiddenMarkovModel model
    
#/**
#* The observation sequence used to calculate probabilities
#*/
    DataSet observationSequence
    
#/**
#* Create a new probability calculator
#* @param model the hidden markov model
#* @param observationSequence the observation sequence
#*/
     ForwardBackwardProbabilityCalculator(HiddenMarkovModel model,
          DataSet observationSequence):
        self.model = model
        self.observationSequence = observationSequence
    }
    
#/**
#* Compute the forward probabilities
#* iterates through time calculating probabilties
#* @return the probability matrix
#*/
     double[][] calculateForwardProbabilities():
        forwardProbabilities = new double[observationSequence.size()][model.getStateCount()]
        scales = new double[observationSequence.size()]
        // intial step
        for (int i = 0 i < model.getStateCount() i++):
            forwardProbabilities[0][i] = 
                model.initialStateProbability(i, observationSequence.get(0))
#* model.observationProbability(i, observationSequence.get(0))
        }
        // apply initial scaling factor
        double sum = 0
        for (int i = 0 i < model.getStateCount() i++):
            sum += forwardProbabilities[0][i]
        }
        scales[0] = 1 / sum
        for (int i = 0 i < model.getStateCount() i++):
            forwardProbabilities[0][i] *= scales[0]
        }
        // recursion
        for (int t = 1 t < observationSequence.size() t++):
            for (int i = 0 i < model.getStateCount() i++):
                // sum over all possible previous states
                // times probability of transitioning
                double priorSum = 0
                for (int j = 0 j < model.getStateCount() j++):
                    priorSum += forwardProbabilities[t - 1][j]
#* model.transitionProbability(j, i, observationSequence.get(t))
                }
                // factor in current observation
                forwardProbabilities[t][i] = priorSum
#* model.observationProbability(i, observationSequence.get(t))
            }
            // apply scaling factor
            sum = 0
            for (int i = 0 i < model.getStateCount() i++):
                sum += forwardProbabilities[t][i]
            }
            scales[t] = 1 / sum
            for (int i = 0 i < model.getStateCount() i++):
                forwardProbabilities[t][i] *= scales[t]
            }
        }
        return forwardProbabilities
    }
    
#/**
#* Compute the backward probabilities
#* iterate backwards through time
#* @return the backward probabilitity matrix
#*/
     double[][] calculateBackwardProbabilities():
        if (scales == null):
            calculateForwardProbabilities()
        }
        backwardProbabilities = new double[observationSequence.size()][model.getStateCount()]
        // inital step
        for (int i = 0 i < model.getStateCount() i++):
            backwardProbabilities[observationSequence.size() - 1][i] = 1
#* scales[observationSequence.size() - 1]
        }
        // recursion
        for (int t = observationSequence.size() - 2 t >= 0 t--):
            for (int i = 0 i < model.getStateCount() i++):
                // sum over possible future states
                double futureSum = 0
                for (int j = 0 j < model.getStateCount() j++):
                    futureSum += model.transitionProbability(i, j, observationSequence.get(t+1))
#* model.observationProbability(j, observationSequence.get(t+1))
#* backwardProbabilities[t+1][j]
                }
                backwardProbabilities[t][i] = futureSum * scales[t]
            }
        }
        return backwardProbabilities
    }
    
#/**
#* Compute the log probability of the observation sequence
#* Calls computerForwardProbabilities if it hasn't been called already
#* @return the log probability
#*/
     double calculateLogProbability():
        if (scales == null):
            calculateForwardProbabilities()
        }
        double sum = 0
        for (int t = 0 t < observationSequence.size() t++):
            sum += Math.log(scales[t])
        }
        return -sum
    }
    
#/**
#* Compute the probability of the observation sequence
#* Calls computerForwardProbabilities if it hasn't been called already
#* @return the log probability
#*/
     double calculateProbability():
        if (scales == null):
            calculateForwardProbabilities()
        }
        double product = 1
        for (int t = 0 t < observationSequence.size() t++):
            product *= scales[t]
        }
        return 1 / product
    }
}
