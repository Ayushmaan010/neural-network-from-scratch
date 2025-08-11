# neuron with n inputs

n = int(input("Enter the no. of inputs:"))
inputs = [0] * n
weights = [0] * n
for i in range(n):
    inputs[i] = float(input("Enter the input: \n"))
    weights[i] = float(input("Enter the weight: \n"))
bias = float(input("Enter the bias: "))
neuron_n = 0
for i in range(len(inputs)):
    neuron_n += inputs[i] * weights[i]
neuron_n += bias
print(neuron_n)
