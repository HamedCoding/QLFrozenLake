# Q Learning / FrozenLake / Not Slippery / 4*4
import gym
import numpy as np
import random
import matplotlib.pyplot as plt
from gym.envs.registration import register
register(
    id='FrozenLakeNotSlippery-v0',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4', 'is_slippery': False},
)
env = gym.make("FrozenLakeNotSlippery-v0")

action_size=env.action_space.n
state_size=env.observation_space.n
q=np.zeros((state_size, action_size))

train_episodes=2000
test_episodes=100
steps=100
gamma=0.9
lr=0.9

epsilon=1
max_epsilon=1
min_epsilon=0.01

decay=0.002

# train
train_wins=[]
epsilon_lst=[]
for episode in range(train_episodes):
    state=env.reset()
    reward=0
    done=False

    for step in range(steps):
        rand_epsilon=random.uniform(0,1)

        if rand_epsilon>epsilon:
            action=np.argmax(q[state,])
        else:
            action=random.randint(0,3)

        new_state, reward, done, info = env.step(action)

        q[state,action]=q[state,action]+lr*(reward+ gamma* np.max(q[new_state,])-q[state,action])

        state = new_state

        if done:
            break

    train_wins.append(reward)
    epsilon=(max_epsilon - min_epsilon) * np.exp(-decay*episode) + min_epsilon
    epsilon_lst.append(epsilon)

print(q)
print(' Mean % score in training= ', round(100*np.mean(train_wins),1))

# test
env.reset()
test_wins=[]
for episode in range(test_episodes):
    state = env.reset()
    done = False
    reward = 0
    state_lst = []
    state_lst.append(state)
    print('******* EPISODE ',episode, ' *******')

    for step in range(steps):
        action = np.argmax(q[state,])
        new_state, reward, done, info = env.step(action)

        q[state, action] = q[state, action] + lr * (reward + gamma * np.max(q[new_state,]) - q[state, action])

        state = new_state
        state_lst.append(state)
        if done:
            print(reward)
            # env.render()
            break

    test_wins.append(reward)
    print('State in each step: ',state_lst)
env.close()

print(' Mean % score in testing= ', int(100*np.mean(test_wins)))

fig=plt.figure(figsize=(10,12))
plt.subplot(311)
plt.plot(list(range(len(train_wins))), train_wins)
plt.plot(list(range(len(train_wins))), len(train_wins)*[np.mean(train_wins)])
plt.title('Train Score')
plt.ylabel('Score')
plt.xlabel('Episode')
plt.legend(['Test score','Mean value'],loc='upper left')

plt.subplot(312)
plt.plot(list(range(len(epsilon_lst))), epsilon_lst)
plt.title('Epsilon')
plt.ylabel('Epsilon')
plt.xlabel('Episode')

plt.subplot(313)
plt.plot(list(range(len(test_wins))), test_wins)
plt.title('Test Score')
plt.ylabel('Score')
plt.xlabel('Episode')

plt.show()
