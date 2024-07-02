import numpy as np

# Input data
x = np.array(([2,9], [1, 9],[3,6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)
x = x / np.amax(x, axis=0)
y=y/100

# Activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid function
def derivation_sigmoid(x):
    return x * (1 - x)

# Neural network parameters
epoch = 5000
lr = 0.1
inputlayer_neurons = 2
hiddenlayer_neurons = 3
outputlayer_neurons = 1

# Initialize weights and biases
wb = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))
bb = np.random.uniform(size=(1, hiddenlayer_neurons))
wout = np.random.uniform(size=(hiddenlayer_neurons,outputlayer_neurons))
bout = np.random.uniform(size=(outputlayer_neurons))

# Training loop
for i in range(epoch):
    hinp1 = np.dot(x, wb)
    hinp = hinp1 + bb
    hlayer_act = sigmoid(hinp)
    outinp1 = np.dot(hlayer_act, wout)
    outinp = outinp1 + bout
    output = sigmoid(outinp)

    EO = y - output  # Ensure y and output have the same shape
    outgrad = derivation_sigmoid(output)
    d_output = EO * outgrad
    EH = d_output.dot(wout.T)
    hiddengrad = derivation_sigmoid(hlayer_act)
    d_hiddenlayer = EH * hiddengrad

    # Weight updates
    wout += hlayer_act.T.dot(d_output) * lr
    wb += x.T.dot(d_hiddenlayer) * lr

print("Input:\n", x)
print("Actual:\n", y)
print("Predicted:\n", output)
