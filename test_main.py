import numpy as np
import gym

import test_State
import test_Agent

import time



if __name__ == "__main__":
    start = time.time()
    ag = test_Agent.Agent()
    ag.play(15)
    # print(ag.showValues())
    # ag.showValuePlot()
    end = time.time()
    print('Iter = 15; gamma = 0.2; time:')
    print(end - start)