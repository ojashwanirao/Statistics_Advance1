#6. Write a Python script to generate random numbers from a Gaussian (normal) distribution and compute the mean, variance, and standard deviation of the samples.

import numpy as np

def generate_random_numbers(mean, std_dev, sample_size):
    """
    Generate random numbers from a Gaussian (normal) distribution.

    Parameters:
    mean (float): Mean of the normal distribution.
    std_dev (float): Standard deviation of the normal distribution.
    sample_size (int): Number of random samples to generate.

    Returns:
    np.ndarray: Array of random samples.
    """
    return np.random.normal(mean, std_dev, sample_size)

def compute_statistics(samples):
    """
    Compute mean, variance, and standard deviation of the samples.

    Parameters:
    samples (np.ndarray): Array of random samples.

    Returns:
    tuple: Mean, variance, and standard deviation of the samples.
    """
    mean = np.mean(samples)
    variance = np.var(samples)
    std_dev = np.std(samples)
    return mean, variance, std_dev

# Parameters for the normal distribution
mean = 0          # Mean of the distribution
std_dev = 1      # Standard deviation of the distribution
sample_size = 1000  # Number of samples to generate

# Generate random numbers
samples = generate_random_numbers(mean, std_dev, sample_size)

# Compute statistics
mean, variance, std_dev = compute_statistics(samples)

# Output the results
print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
