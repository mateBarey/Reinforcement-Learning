# Reinforcement-Learning

The following is a Reinforcement Learning approach that uses Actor Critic Policies to arrive at the 

best solution for a cart pole balancing problem. The program uses an actor neural network to find the best policies 

and then uses a sister Critic network which assigns probabliities for the best actions. The best actions and 

probabilities for each action are then rewarded and discounted. Where each loss in reward is the difference 

between a discounted actor and crtic state. The Actor reward is maximized by taking the -log of the the difference 

in state plus the discounted reward. This is then added to the Critic loss which is the change in states plus the discounted 

reward squared. The gradient of the sum of these functions is found in order to adjust each neural networks weights 

 through backpropagation. Currently Havent achieved a high score.
 
 
 I will be updating this program soon with a short term memory 
 
 option that should improve the algorithm.
