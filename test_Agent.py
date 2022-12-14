import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

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

        Bed, Liv, Entr, Din, Off = test_MoveProb.MoveProb()

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

    def chooseAction(self, MoveProbMat):
        # choose action with most expected value
        mx_nxt_reward = 0
        action = ""

        if np.random.uniform(0, 1) <= self.exp_rate:
            action = np.random.choice(self.actions)
        else:
            # greedy action
            for a in self.actions:
                # if the action is deterministic
                nxt_reward = self.state_values[self.State.nxtPosition(a, MoveProbMat)]
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
        MoveProbMat = self.checkRoomMoveProb()
        while i < rounds:
            # to the end of game back propagate reward
            if self.State.isEnd:
                # back propagate
                reward = self.State.giveReward()
                # explicitly assign end state to reward values
                self.state_values[self.State.state] = reward  # this is optional
                # print("Game End Reward", reward)
                for s in reversed(self.states):
                    reward = self.state_values[s] + self.lr * (reward - self.state_values[s])
                    self.state_values[s] = round(reward, 3)
                self.reset()
                i += 1
            else:
                action = self.chooseAction(MoveProbMat)
                # append trace
                self.states.append(self.State.nxtPosition(action, MoveProbMat))
                # print("current position {} action {}".format(self.State.state, action))
                # by taking the action, it reaches the next state
                self.State = self.takeAction(action, MoveProbMat)
                # mark is end
                self.State.isEndFunc()
                # print("nxt state", self.State.state)
                # print("---------------------")

    def showValues(self):
        for i in range(0, BOARD_ROWS):
            # print('----------------------------------')
            # out = '| '
            for j in range(0, BOARD_COLS):
                out += str(self.state_values[(i, j)]).ljust(6) + ' | '
            # print(out)
        # print('----------------------------------')

    def showValuePlot(self):
        output_Val = []

        room = ["Bottom: Kitcken | Top: Stairs", "Bottom: Dinning room | Top: Bedroom", "Bottom: Office | Top: Living room", "Bottom:Bathroom | Top: Entrance"]

        for i in range(0, BOARD_ROWS):
            for j in range(0, BOARD_COLS):
                output_Val.append(self.state_values[(i, j)])
        output_Val = np.array(output_Val)
        output_Val = np.reshape(output_Val,(2,4))
        # print(output_Val)

        fig, ax = plt.subplots()
        im = ax.imshow(output_Val)

        ax.set_xticks(np.arange(len(room)))
        ax.set_xticklabels(room)
        ax.set_yticks(np.arange(2))

        plt.setp(ax.get_xticklabels(), rotation=20, ha="right",
         rotation_mode="anchor")

        for i in range(2):
            for j in range(4):
                text = ax.text(j, i, output_Val[i, j],
                            ha="center", va="center", color="w")

        ax.set_title("Expected Value After " + "15" + " Iterations with Discount Factor = " + "0.2" )
        fig.tight_layout()
        plt.show()