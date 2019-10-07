import numpy as np


def neural_network(input, weights):
    pred = vect_mul_sum(input, weights)
    return pred


def vect_mul_sum(vec, matrix):
    assert(len(vec) == len(matrix))
    output = [0, 0, 0]

    for i in range(len(vec)):
        output[i] = round(vec.dot(matrix[i]), 5)

    return output


weights = [
    [0.1, 0.1, -0.3],
    [0.1, 0.2, 0.0],
    [0.0, 1.3, 0.1]
]

toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

for i in range(len(toes)):
    input = np.array([toes[i], wlrec[i], nfans[i]])
    pred = neural_network(input, weights)
    print(pred)
