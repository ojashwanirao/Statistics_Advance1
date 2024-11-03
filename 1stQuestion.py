#1. Generate a list of 100 integers containing values between 90 to 130 and store it in the variable `int_list`. After generating the list, find the following:

#(i) Write a Python function to calculate the mean of a given list of numbers.
#Create a function to find the median of a list of numbers.
#(ii) Develop a program to compute the mode of a list of integers.
#(iii) Implement a function to calculate the weighted mean of a list of values and their corresponding weights.
#(iv) Write a Python function to find the geometric mean of a list of positive numbers.
#(v) Create a program to calculate the harmonic mean of a list of values.
#(vi) Build a function to determine the midrange of a list of numbers (average of the minimum and maximum).
#(vii) Implement a Python program to find the trimmed mean of a list, excluding a certain percentage of outliers.

import numpy as np
from scipy import stats
from collections import Counter

# Generate a list of 100 integers between 90 to 130
int_list = np.random.randint(90, 131, size=100)

# (i) Function to calculate the mean
def calculate_mean(data):
    return np.mean(data)

# Function to find the median
def calculate_median(data):
    return np.median(data)

# (ii) Function to compute the mode using Counter
def calculate_mode(data):
    count = Counter(data)
    mode_data = count.most_common(1)
    return mode_data[0][0], mode_data[0][1]  # Return mode value and its count

# (iii) Function to calculate the weighted mean
def calculate_weighted_mean(data, weights):
    return np.average(data, weights=weights)

# (iv) Function to find the geometric mean
def calculate_geometric_mean(data):
    return stats.gmean(data)

# (v) Function to calculate the harmonic mean
def calculate_harmonic_mean(data):
    return stats.hmean(data)

# (vi) Function to determine the midrange
def calculate_midrange(data):
    return (np.min(data) + np.max(data)) / 2

# (vii) Function to find the trimmed mean
def calculate_trimmed_mean(data, proportion_to_trim):
    return stats.trim_mean(data, proportion_to_trim)

# Example usage of the functions
if __name__ == "__main__":
    print("Generated List:", int_list[:10], "...")  # Display the first 10 numbers

    # (i)
    mean_value = calculate_mean(int_list)
    median_value = calculate_median(int_list)
    print("Mean:", mean_value)
    print("Median:", median_value)

    # (ii)
    mode_value, mode_count = calculate_mode(int_list)
    print("Mode: Value =", mode_value, "Count =", mode_count)

    # (iii)
    weights = np.random.rand(100)  # Generate random weights for the weighted mean
    weighted_mean = calculate_weighted_mean(int_list, weights)
    print("Weighted Mean:", weighted_mean)

    # (iv)
    geometric_mean = calculate_geometric_mean(int_list)
    print("Geometric Mean:", geometric_mean)

    # (v)
    harmonic_mean = calculate_harmonic_mean(int_list)
    print("Harmonic Mean:", harmonic_mean)

    # (vi)
    midrange_value = calculate_midrange(int_list)
    print("Midrange:", midrange_value)

    # (vii)
    trimmed_mean = calculate_trimmed_mean(int_list, proportion_to_trim=0.1)  # Trim 10% from both ends
    print("Trimmed Mean (10%):", trimmed_mean)
