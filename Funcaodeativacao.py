import numpy as np

def stepfunction(soma):
    if(soma >= 1):
        return 1
    return 0 

def sigmoidfunction(soma):
    return 1/(1+np.exp(-soma))

def tahnfunction(soma):
    return (np.exp(soma) - np.exp(-soma))/(np.exp(soma) + np.exp(-soma))

def relufunction(soma):
    if(soma >= 0):
        return soma
    return 0;

def linearfunction(soma):
    return soma

def softmaxfunction(x):
    ex = np.exp(x)
    return ex/ex.sum()
    
test = stepfunction(-1)
test = sigmoidfunction(2.1)
test = tahnfunction(2.1)
test = relufunction(0.358)
test = linearfunction(0.358)
valores = [5.0,2.0,1.3]
print(softmaxfunction(valores))

((((1 - 0.3)**2) + (0.02**2) + ((1 - 0.89)**2) + (0.320**2)))/4

((1-0.3) + (0.02) + (1 - 0.89) + (0.320))/4