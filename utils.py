import matplotlib as plt
import numpy as np

def plotLearning(scores, filename, x=None, window=5):
    N = len(scores)
    running_avg = np.empty(N)
    for t in range(N):
	    running_avg[t] = np.mean(scores[max(0, t-window):(t+1)])
    if x is None:
        x = [i for i in range(N)]
    plt.ylabel('Score')
    plt.xlabel('Game')
    plt.plot(x, running_avg)
    plt.savefig(filename)


print('big' > 'small')


def frac_part(numerator,denominator):
    if numerator%denominator == 0:
       return 0
    else:
        return (numerator%denominator)/denominator

print(frac_part(5,4))
print(1%2)


def smallest_prime_factor(x):
    """Returns the smallest prime number that is a divisor of x"""
    # Start checking with 2, then move up one by one
    n = 2
    while n <= x:
        if x % n == 0:
            return n
        elif x % (n+1) == 0:
            return (n+1)

print(smallest_prime_factor(12)) # should be 2
print(smallest_prime_factor(15)) # should be 3
