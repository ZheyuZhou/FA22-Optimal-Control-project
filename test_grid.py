import gym
import time 

env = gym.make('GridWorld-v1')
env.reset()
env.render()
time.sleep(10)
env.close()