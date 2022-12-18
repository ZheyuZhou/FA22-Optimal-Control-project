#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gym
env = gym.make('homemadeGrid')
env.reset()
for _ in range(1000):
    env.render()
    # take a random action
    env.step(env.action_space.sample()) 
env.close()