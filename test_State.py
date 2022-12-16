import numpy as np

# global variables
BOARD_ROWS = 2
BOARD_COLS = 4
WIN_STATE = (1, 0)
LOSE_STATE = (0, 0)
START = (0, 3)
DETERMINISTIC = True

class State:
    def __init__(self, state=START):
        self.board = np.zeros([BOARD_ROWS, BOARD_COLS])
        self.board[1, 3] = -1
        self.state = state
        self.isEnd = False
        self.determine = DETERMINISTIC

    def giveReward(self):
        if self.state == WIN_STATE:
            return 1
        elif self.state == LOSE_STATE:
            return -1
        else:
            return 0

    def isEndFunc(self):
        if (self.state == WIN_STATE) or (self.state == LOSE_STATE):
            self.isEnd = True

    def nxtPositionProb(self):
        return 0

    def nxtPosition(self, action, MoveProbMat):
        """
        action: up, down, left, right
        -------------
        0 | 1 | 2| 3|
        1 |
        2 |
        return next position
        """
        if self.determine:   
            
            # call nxtPositionProb

            if action == "up":
                row = 2

                # MoveProb = np.max(MoveProbMat[row])
                StayProb = np.sort(MoveProbMat[row])[-2]
                if np.random.uniform(0,1,1) < StayProb:
                    nxtState = (self.state[0], self.state[1])
                else:
                    nxtState = (self.state[0] - 1, self.state[1])

                # print(self.state, 'self.state, up', type(self.state))

            elif action == "down":
                row = 3

                # MoveProb = np.max(MoveProbMat[row])
                StayProb = np.sort(MoveProbMat[row])[-2]
                if np.random.uniform(0,1,1) < StayProb:
                    nxtState = (self.state[0], self.state[1])
                else:
                    nxtState = (self.state[0] + 1, self.state[1])
                    
            elif action == "left":
                row = 0

                # MoveProb = np.max(MoveProbMat[row])
                StayProb = np.sort(MoveProbMat[row])[-2]
                if np.random.uniform(0,1,1) < StayProb:
                    nxtState = (self.state[0], self.state[1])
                else:
                    nxtState = (self.state[0], self.state[1] - 1)
            else:
                row = 1

                # MoveProb = np.max(MoveProbMat[row])
                StayProb = np.sort(MoveProbMat[row])[-2]
                if np.random.uniform(0,1,1) < StayProb:
                    nxtState = (self.state[0], self.state[1])
                else:
                    nxtState = (self.state[0], self.state[1] + 1)

            # if next state legal
            if (nxtState[0] >= 0) and (nxtState[0] <= (BOARD_ROWS -1)):
                if (nxtState[1] >= 0) and (nxtState[1] <= (BOARD_COLS -1)):
                    if nxtState != (1, 3):
                        return nxtState
            return self.state

    def showBoard(self):
        self.board[self.state] = 1
        for i in range(0, BOARD_ROWS):
            print('-----------------')
            out = '| '
            for j in range(0, BOARD_COLS):
                if self.board[i, j] == 1:
                    token = '*'
                if self.board[i, j] == -1:
                    token = 'z'
                if self.board[i, j] == 0:
                    token = '0'
                out += token + ' | '
            print(out)
        print('-----------------')