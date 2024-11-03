#10. Write a Python function to calculate the probability mass function (PMF) of Poisson distribution.

import math

def poisson_pmf(lamb, k):
    """
    Calculate the probability mass function (PMF) of a Poisson distribution.

    Parameters:
    lamb (float): The average rate (λ) of events occurring.
    k (int): The actual number of events.

    Returns:
    float: The probability of observing exactly k events.
    """
    return (math.exp(-lamb) * (lamb ** k)) / math.factorial(k)

# Example usage
lamb = 3  # average rate of events
k = 2     # number of events
print("PMF of Poisson distribution:", poisson_pmf(lamb, k))
