import numpy as np

import test_State
import test_MoveProb

# global variables
BOARD_ROWS = 2
BOARD_COLS = 4
WIN_STATE = (1, 0)
LOSE_STATE = (0, 0)
START = (0, 3)
DETERMINISTIC = True


# Agent of player

class Agent:

    def __init__(self):
        self.states = []
        self.actions = ["up", "down", "left", "right"]
        self.State = test_State.State()
        self.lr = 0.2 # gamma discount factor
        self.exp_rate = 0.3

        # initial state reward
        self.state_values = {}
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                self.state_values[(i, j)] = 0  # set initial value to 0

    def checkRoomMoveProb(self):

        # Check room and return prob
        """
            0       1     2     3    col 
            ----------------------------  
          0 | Stair | Bed | Liv | Entr |   
          1 | Kit   | Din | Off | Bath |
        row ----------------------------
        """

        currentPosition = self.State.state

        Bed, Liv, Entr, Kit, Din, Off = test_MoveProb.MoveProb()

        if currentPosition == (0,1): # Bed
            MoveProbMat = Bed
        if currentPosition == (0,2): # Liv
            MoveProbMat = Liv
        if currentPosition == (0,3): # Entr
            MoveProbMat = Entr
        if currentPosition == (1,1): # Din
            MoveProbMat = Din
        if currentPosition == (1,2): # Off
            MoveProbMat = Off
        return MoveProbMat

    def chooseAction(self):
        # choose action with most expected value
        mx_nxt_reward = 0
        action = ""

        if np.random.uniform(0, 1) <= self.exp_rate:
            action = np.random.choice(self.actions)
        else:
            # greedy action
            for a in self.actions:
                # if the action is deterministic
                nxt_reward = self.state_values[self.State.nxtPosition(a)]
                if nxt_reward >= mx_nxt_reward:
                    action = a
                    mx_nxt_reward = nxt_reward
        return action

    def takeAction(self, action, MoveProbMat):
        position = self.State.nxtPosition(action, MoveProbMat)
        return test_State.State(state=position)

    def reset(self):
        self.states = []
        self.State = test_State.State()

    def play(self, rounds=10):
        i = 0
        while i < rounds:
            # to the end of game back propagate reward
            if self.State.isEnd:
                # back propagate
                reward = self.State.giveReward()
                # explicitly assign end state to reward values
                self.state_values[self.State.state] = reward  # this is optional
                print("Game End Reward", reward)
                for s in reversed(self.states):
                    reward = self.state_values[s] + self.lr * (reward - self.state_values[s])
                    self.state_values[s] = round(reward, 3)
                self.reset()
                i += 1
            else:
                action = self.chooseAction()
                # append trace
                self.states.append(self.State.nxtPosition(action))
                print("current position {} action {}".format(self.State.state, action))
                # by taking the action, it reaches the next state
                self.State = self.takeAction(action)
                # mark is end
                self.State.isEndFunc()
                print("nxt state", self.State.state)
                print("---------------------")

    def showValues(self):
        for i in range(0, BOARD_ROWS):
            print('----------------------------------')
            out = '| '
            for j in range(0, BOARD_COLS):
                out += str(self.state_values[(i, j)]).ljust(6) + ' | '
            print(out)
        print('----------------------------------')