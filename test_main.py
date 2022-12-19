import numpy as np
import gym

import test_State
import test_Agent


if __name__ == "__main__":
    ag = test_Agent.Agent()
    # ag.play(20)
    ag.play(5)
    print(ag.showValues())
    ag.showValuePlot()