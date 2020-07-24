# Posterior-Proabilites

# The task in this part is to implement a system that:
Can determine the posterior probability of different hypotheses, given priors for these hypotheses, and given a sequence of observations.
Can determine the probability that the next observation will be of a specific type, priors for different hypotheses, and given a sequence of observations.

There are five types of bags of candies. Each bag has an infinite amount of candies. We have one of those bags, 
and we are picking candies out of it. We don't know what type of bag we have, 
so we want to figure out the probability of each type based on the candies that we have picked.

# The five possible hypotheses for our bag are:

h1 (prior: 10%): This type of bag contains 100% cherry candies.
h2 (prior: 20%): This type of bag contains 75% cherry candies and 25% lime candies.
h3 (prior: 40%): This type of bag contains 50% cherry candies and 50% lime candies.
h4 (prior: 20%): This type of bag contains 25% cherry candies and 75% lime candies.
h5 (prior: 10%): This type of bag contains 100% lime candies.

# Command Line arguments:

The program takes a single command line argument, which is a string, for example CLLCCCLLL. 
This string represents a sequence of observations, i.e., a sequence of candies that we have already picked. 
Each character is C if we picked a cherry candy, and L if we picked a lime candy.
Assuming that characters in the string are numbered starting with 1, the i-th character of the string corresponds to the i-th observation. 

The program should be invoked from the commandline as follows:
compute_a_posteriori observations
For example:
compute_a_posteriori CLLCCLLLCCL
We also allow the case of not having a command line argument at all, this represents the case where we have made no observations yet.

# Output:

Our program should create a text file called "result.txt", that is formatted exactly as shown below. ??? is used where our program should print values that depend on its command line argument. 
Five decimal points should appear for any floating point number.
Observation sequence Q: ???
Length of Q: ???

After Observation ??? = ???: (This and all remaining lines are repeated for every observation)

P(h1 | Q) = ???
P(h2 | Q) = ???
P(h3 | Q) = ???
P(h4 | Q) = ???
P(h5 | Q) = ???

Probability that the next candy we pick will be C, given Q: ???
Probability that the next candy we pick will be L, given Q: ???
