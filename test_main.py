import numpy as np

import test_State
import test_Agent


if __name__ == "__main__":
    ag = test_Agent.Agent()
    ag.play(50)
    print(ag.showValues())
    