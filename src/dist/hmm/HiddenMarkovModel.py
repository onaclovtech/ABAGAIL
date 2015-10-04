


#/**
#* The abstraction of a hidden markov model
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 interface HiddenMarkovModel extends Serializable {
#/**
#* Get the state count for self model
#* @return the number of states in the model
#*/
     abstract int getStateCount()
#/**
#* Sample a next state given the current state and input
#* @param i the current state
#* @param o the input value
#* @return the next state
#*/
     abstract int sampleState(int i, Instance o)
#/**
#* Sample the initial state given the current state
#* @param o the input value
#* @return the initial state
#*/
     abstract int sampleInitialState(Instance o)
#/**
#* Sample an input given the current observation
#* @param i the current state
#* @param o the input value
#* @return the sample observation
#*/
     abstract Instance sampleObservation(int i, Instance o)
#/**
#* Get the initial state probability
#* @param i the initial state
#* @param o the initial observation
#* @return the probability
#*/
     abstract double initialStateProbability(int i, Instance o)
#/**
#* Get the probability of transitioning from state i to state j,
#* with observation o
#* @param i the first state
#* @param j the second state
#* @param o the observation at state i
#* @return the probability
#*/
     abstract double transitionProbability(int i, int j, Instance o)
#/**
#* Get the probability of observing o in state i
#* @param i the current state
#* @param o the observation
#* @param in the corresponding input
#* @return the probability
#*/
     abstract double observationProbability(
        int i, Instance o)
#/**
#* Match the outputs in state i to the given expectaions for the given 
#* sequence
#* @param i the state 
#* @param expectations the expectations
#* @param sequence the sequence
#*/
     abstract  estimateOutputDistribution(
        int i, DataSet sequence)
#/**
#* Match the initial state distribution to the given expectations 
#* for the initial observation data
#* @param expectations [k][i] is the expected times in state i initially
#* for observation sequence k
#* @param observations the observation sequence
#*/
     abstract  estimateIntialStateDistribution(
        double[][] expectations,
        DataSet observation)
#/**
#* Match the transitions in state i to the given expectations for the
#* transition observation data
#* @param i the start state
#* @param expectations the expected transitions [t][j] for time t to state j
#* @param sequence the transition observatiosn
#* @param sequence the observation sequence
#*/
     abstract  estimateTransitionDistribution(
        int i,
        double[][] expectations,
        DataSet observations)
}