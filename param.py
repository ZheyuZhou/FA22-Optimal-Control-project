import numpy as np

class Param_:
    def __init__(self, P_transition):
        self.P_transition = P_transition

    def P_transition_Matrix(self):
        ### X1 State: L O B D K
        ### A1 Action: L R U D
        ### Conditional Probability: L O B D K
        Liv = np.array([
        #   L   O   B   D   K
            [0.3, 0, 0.7, 0, 0], # L
            [1, 0, 0, 0, 0], # R
            [1, 0, 0, 0, 0], # U
            [0.3, 0.7, 0, 0, 0] #D
        ])
    
        Off = np.array([
        #   L   O   B   D   K
            [0, 0.3, 0, 0.7, 0], # L
            [0, 1, 0, 0, 0], # R
            [0.7, 0.3, 0, 0, 0], # U
            [0, 1, 0, 0, 0] #D
        ])

        Bed = np.array([
        #   L   O   B   D   K
            [0, 0, 1, 0, 0], # L
            [0.7, 0, 0.3, 0, 0], # R
            [0, 0, 1, 0, 0], # U
            [0, 0, 0.3, 0.7, 0] #D
        ])

        Din = np.array([
        #   L   O   B   D   K
            [0, 0, 0, 0.3, 0.7], # L
            [0, 0.7, 0, 0.3, 0], # R
            [0, 0, 0.7, 0.3, 0], # U
            [0, 0, 0, 1, 0] #D
        ])

        Kit = np.array([
        #   L   O   B   D   K
            [0, 0, 0, 0, 1], # L
            [0, 0, 0, 0.7, 0.3], # R
            [0, 0, 0, 0, 1], # U
            [0, 0, 0, 0, 1] #D
        ])


        P_trainstion_L = np.vstack((Liv[0], Off[0], Bed[0], Din[0], Kit[0]))
        P_trainstion_R = np.vstack((Liv[1], Off[1], Bed[1], Din[1], Kit[1]))
        P_trainstion_U = np.vstack((Liv[2], Off[2], Bed[2], Din[2], Kit[2]))
        P_trainstion_D = np.vstack((Liv[3], Off[3], Bed[3], Din[3], Kit[3]))

        return P_trainstion_L, P_trainstion_R, P_trainstion_U, P_trainstion_D