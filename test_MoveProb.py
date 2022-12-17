import numpy as np


def MoveProb():
    ### X1 State: Stair Bed Liv Entr Din Off Bath
    ### A1 Action: L R U D
    ### Conditional Probability: Bed Liv Entr Din Off

    Bed = np.array([
    #   S	Bed	 L 	E	K	D	O	Bath
        [0.7, 0.3, 0, 0, 0,	0, 0, 0], # L
        [0,	0.3, 0.7, 0, 0,	0, 0, 0], # R
        [0, 1, 0, 0, 0, 0, 0, 0], # U
        [0,	0.3, 0, 0, 0, 0.7, 0, 0] #D
    ])


    Liv = np.array([
    #   S	Bed	 L 	E	K	D	O	Bath
        [0, 0.7, 0.3, 0, 0, 0, 0, 0], # L
        [0, 0, 0.3, 0.7, 0, 0, 0, 0], # R
        [0, 0, 1, 0, 0, 0, 0, 0], # U
        [0, 0, 0.3, 0, 0, 0, 0.7, 0] #D
    ])

    Entr = np.array([
    #   S	Bed	 L 	E	K	D	O	Bath
        [0, 0, 0.7, 0.3, 0, 0, 0, 0], # L
        [0, 0, 0, 1, 0, 0, 0, 0], # R
        [0, 0, 0, 1, 0, 0, 0, 0], # U
        [0, 0, 0, 0.3, 0, 0, 0, 0.7] #D
    ])

    # Kit = np.array([
    # #   S	Bed	 L 	E	K	D	O	Bath
    #     [0, 0, 0, 0, 1, 0, 0, 0], # L
    #     [0, 0, 0, 0, 0.3, 0.7, 0, 0], # R
    #     [0.7, 0, 0, 0, 0.3, 0, 0, 0], # U
    #     [0, 0, 0, 0, 1, 0, 0, 0] #D
    # ])

    Din = np.array([
    #   S	Bed	 L 	E	K	D	O	Bath
        [0, 0, 0, 0, 0.7, 0.3, 0, 0], # L
        [0, 0, 0, 0, 0, 0.3, 0.7, 0], # R
        [0, 0.7, 0, 0, 0, 0.3, 0, 0], # U
        [0, 0, 0, 0, 0, 1, 0, 0] #D
    ])

    Off = np.array([
    #   S	Bed	 L 	E	K	D	O	Bath
        [0, 0, 0, 0, 0, 0.7, 0.3, 0], # L
        [0, 0, 0, 0, 0, 0, 0.3, 0.7], # R
        [0, 0, 0.7, 0, 0, 0, 0.3, 0], # U
        [0, 0, 0, 0, 0, 0, 1, 0] #D
    ])
    


    # P_trainstion_L = np.vstack((Liv[0], Off[0], Bed[0], Din[0],))
    # P_trainstion_R = np.vstack((Liv[1], Off[1], Bed[1], Din[1], Kit[1]))
    # P_trainstion_U = np.vstack((Liv[2], Off[2], Bed[2], Din[2], Kit[2]))
    # P_trainstion_D = np.vstack((Liv[3], Off[3], Bed[3], Din[3], Kit[3]))

    return Bed, Liv, Entr, Din, Off