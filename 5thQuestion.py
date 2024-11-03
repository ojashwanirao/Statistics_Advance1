#5. Create a Python function to generate random samples from a given probability distribution (e.g., binomial, Poisson) and calculate their mean and variance.

import numpy as np

def generate_samples(distribution, *params, sample_size=1000):
    """
    Generate random samples from a given probability distribution and calculate their mean and variance.

    Parameters:
    distribution (str): The type of distribution ('binomial' or 'poisson').
    *params: Parameters required for the distribution.
             For binomial: n (number of trials), p (probability of success)
             For poisson: lambda (average rate of events)
    sample_size (int): Number of random samples to generate.

    Returns:
    tuple: Array of random samples, mean of the samples, variance of the samples.
    """
    if distribution == 'binomial':
        n, p = params
        samples = np.random.binomial(n, p, sample_size)
    elif distribution == 'poisson':
        lamb = params[0]
        samples = np.random.poisson(lamb, sample_size)
    else:
        raise ValueError("Unsupported distribution type. Use 'binomial' or 'poisson'.")

    mean = np.mean(samples)
    variance = np.var(samples)
    
    return samples, mean, variance

# Example usage for Binomial distribution
try:
    binomial_samples, binomial_mean, binomial_variance = generate_samples('binomial', n=10, p=0.5)
    print("Binomial Distribution Samples:", binomial_samples)
    print("Mean (Binomial):", binomial_mean)
    print("Variance (Binomial):", binomial_variance)

    # Example usage for Poisson distribution
    poisson_samples, poisson_mean, poisson_variance = generate_samples('poisson', 5)  # Lambda is 5
    print("\nPoisson Distribution Samples:", poisson_samples)
    print("Mean (Poisson):", poisson_mean)
    print("Variance (Poisson):", poisson_variance)

except Exception as e:
    print("An error occurred:", e)
