import numpy as np


def neural_network(input, weights):
    pred = input.dot(weights)
    return pred


weights = [0.1, 0.2, 0.0]

toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

for i in range(len(toes)):
    input = np.array([toes[i], wlrec[i], nfans[i]])
    pred = neural_network(input, weights)
    print(round(pred, 2))
