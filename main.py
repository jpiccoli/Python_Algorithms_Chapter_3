import math
import matplotlib.pyplot as plt

def revenue(tax):
    return(100 * (math.log(tax +1) - (tax - 0.2)**2 + 0.04))

def revenue_derivative(tax):
    return(100 * (1/(tax + 1) - 2 * (tax - 0.2)))

def calculate_rate():
    step_size = 0.001
    threshold = 0.0001
    maximum_iterations = 100000
    current_rate = 0.7
    iterating = True
    iterations  = 0
    while(iterating):
        rate_change = step_size * revenue_derivative(current_rate)
        current_rate = current_rate + rate_change

        if(abs(rate_change) < threshold):
            break

        if(iterations > maximum_iterations):
            break

        iterations= iterations + 1

    print('Current rate = ' + str(current_rate))
    return current_rate


########################################################################

xs = [x/1000 for x in range(1001)]
ys =[revenue(x) for x in xs]
plt.plot(xs, ys)
current_rate = calculate_rate()
plt.plot(current_rate, revenue(current_rate), 'ro')
plt.title('Tax Rates and Revenue')
plt.xlabel('Tax Rate')
plt.ylabel('Revenue')
plt.show()