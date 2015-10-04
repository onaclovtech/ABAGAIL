
#/**
#* A discrete markov decision process
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 interface MarkovDecisionProcess {
#/** An ok default gamma value */
     static final double GAMMA = .9
#/**
#* Get the number of states in the mdp
#* @return the number of states
#*/
     int getStateCount()
#/**
#* Get the number of actions in the mdp
#* @return the number of actions
#*/
     int getActionCount()
#/**
#* Get the reward for a state and action
#* @param state the state
#* @param action the action
#* @return the reward
#*/
     abstract double reward(int state, int action)
#/**
#* Get the probability of transitioning from state i to state j,
#* with observation o
#* @param i the first state
#* @param j the second state
#* @param a the action
#* @return the probability
#*/
     abstract double transitionProbability(int i, int j, int a)

#/**
#* Sample a next state given the current state and input
#* @param i the current state
#* @param a the action
#* @return the next state
#*/
     abstract int sampleState(int i, int a)
#/**
#* Get the initial state
#* @return the initial state
#*/
     abstract int sampleInitialState()
#/**
#* Check if a state is terminal
#* @param state the state
#* @return true if it is
#*/
     abstract boolean isTerminalState(int state)
}