import numpy as np
import gym

import test_State
import test_Agent



if __name__ == "__main__":
    ag = test_Agent.Agent()
    ag.play(60)
    print(ag.showValues())
    