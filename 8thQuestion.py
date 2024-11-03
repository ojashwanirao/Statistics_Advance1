#8. Write a Python function to calculate the probability density function (PDF) of a continuous random variable for a given normal distribution.

import math

def normal_pdf(x, mu, sigma):
    """
    Calculate the probability density function (PDF) of a normal distribution.

    Parameters:
    x (float): The point at which to calculate the PDF.
    mu (float): The mean of the distribution.
    sigma (float): The standard deviation of the distribution.

    Returns:
    float: The probability density at x.
    """
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Example usage
mu = 0      # mean of the distribution
sigma = 1   # standard deviation of the distribution
x = 1       # point at which PDF is calculated
print("PDF of Normal distribution:", normal_pdf(x, mu, sigma))
