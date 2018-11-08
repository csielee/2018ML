import math
import random

def Marsaglia():
    while True:
        U = random.random()*2-1
        V = random.random()*2-1
        if (U**2)+(V**2) < 1:
            break
    
    S = (U**2)+(V**2)
    S = math.sqrt((-2*math.log(S))/S)
    return (U*S, V*S)

def GaussianDataGenerator(u, v):
    sigma = math.sqrt(v)
    while True:
        D1, D2 = Marsaglia()
        yield u + sigma*D1
        yield u + sigma*D2