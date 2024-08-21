import math
import matplotlib.pyplot as plt

def revenue(tax):
    return(100 * (math.log(tax +1) - (tax - 0.02)**2 + 0.04))