import dataset as data
import numpy as np

def sig(x):
    return 2*(1/(1 + np.exp(-x))) - 1

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def w_evaluation(input_vector_of_vectors, w_initial, d):
    w_old = w_initial
    delta = 1
    count = 0
    bias = -1
    learning_rate = 0.1
    y = []
    while count != 24:
        count = 0
        for l in range(len(input_vector_of_vectors)):
            w_old[0] = bias
            y_response = sig(w_old.T @ input_vector_of_vectors[l])
            w_new = w_old + learning_rate * ((d[l] - y_response) * input_vector_of_vectors[l])
            w_new[0] = bias
            delta = np.sqrt(np.sum(np.power((w_new - w_old), 2)))
            w_old = w_new
            y.append(truncate(y_response, 2))
            if delta < 0.001:
                count += 1
                #print(count)

    print('\n' + "End of training" + '\n')
    #print(y[(len(y) - 24):])
    return w_old, y[(len(y) - 24):]

def w_evaluation_steepest_descent(input_vector_of_vectors, w_initial, d):
    w_old = w_initial
    learning_rate = 0.1
    y = []
    sum = np.resize(np.ones(65), (65, 1))

    
    while sum.any():
        sum = np.resize(np.zeros(65), (65, 1))
        for l in range(len(input_vector_of_vectors)):
            y_response = sig(w_old.T @ input_vector_of_vectors[l])
            delta = d[l] - y_response
            if delta < 0:
                delta *= -1
            if delta > 0.01:
                sum += (input_vector_of_vectors[l] * d[l])
            y.append(truncate(y_response, 2))
        if sum.any():
            w_new = w_old + sum * learning_rate
        else:
            w_new = w_old
        w_old = w_new

    print('\n' + "End of training" + '\n')
    return w_old, y[(len(y) - 24):]

def initialization(letter):
    input_vector_of_matrices, d = data.image_preprocessor(letter)
    input_vector_of_vectors = []
    w_initial = np.reshape(np.zeros(65), [65, 1])
    for i in range(len(input_vector_of_matrices)):
        input_vector_of_vectors.append(np.reshape(input_vector_of_matrices[i], [64, 1]))
        input_vector_of_vectors[i] = np.insert(input_vector_of_vectors[i], 0, 1, axis=0)
    
    # return w_evaluation(input_vector_of_vectors, w_initial, d)
    return w_evaluation_steepest_descent(input_vector_of_vectors, w_initial, d)

if __name__ == '__main__':
    initialization()