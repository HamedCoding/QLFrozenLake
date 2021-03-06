# Q Learning Plays 4*4 Frozen Lake (Not Slippery)

In this example, reinforcement learning method (Q Learning) makes its effort to learn 4*4 Frozen Lake.  
The game environment is like the following:

<p align="center">
  <img src="https://github.com/hamedmkazemi/QLearning_FrozenLake_1/blob/main/images/FrozenLake.png" alt="Sublime's custom image"/>
</p>

Or:
  
SFFF  
FHFH  
FFFH  
HFFG  
  
S: starting point, safe  
F: frozen surface, safe  
H: hole, fall to your doom  
G: goal, where the frisbee is located  
  
The agent should start from start position (state: 0), and reach the goal (state: 15) by walikng in the frozen areas. If the agent reach the goal cell, it gets a reward (1.0).  
  
We have 16 states and 4 actions. It should be noted that the action numbers map to the following directions:  
Action: Direction  
0:  Left  
1:  Down  
2:  Right  
3:  Up  
  
  
The final result:  

<p align="center">
  <img src="https://github.com/hamedmkazemi/QLearning_FrozenLake_1/blob/main/images/result.png" alt="Sublime's custom image"/>
</p>
