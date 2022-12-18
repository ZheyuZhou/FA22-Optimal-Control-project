import gym
import time 

env = gym.make('GridWorld-v1')
env.reset()
env.render()
time.sleep(2)
env.close()