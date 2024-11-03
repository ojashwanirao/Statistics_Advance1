#2. Generate a list of 500 integers containing values between 200 to 300 and store it in the variable `int_list2`.
#After generating the list, find the following:
#(i) Compare the given list of visualization for the given data:
#1. Frequency & Gaussian distribution
#2. Frequency smoothened KDE plot
#3. Gaussian distribution & smoothened KDE plot
#(ii) Write a Python function to calculate the range of a given list of numbers.
#(iii) Create a program to find the variance and standard deviation of a list of numbers.
#(iv) Implement a function to compute the interquartile range (IQR) of a list of values.
#(v) Build a program to calculate the coefficient of variation for a dataset.
#(vi) Write a Python function to find the mean absolute deviation (MAD) of a list of numbers.
#(vii) Create a program to calculate the quartile deviation of a list of values.
#(viii) Implement a function to find the range-based coefficient of dispersion for a dataset.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# (i) Generate a list of 500 integers between 200 to 300
int_list2 = np.random.randint(200, 301, size=500)

# Visualization of the generated data
def visualize_data(data):
    plt.figure(figsize=(12, 8))

    # Frequency distribution
    plt.subplot(2, 2, 1)
    plt.hist(data, bins=30, alpha=0.5, color='blue', density=True, label='Frequency')
    plt.title('Frequency Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    
    # Gaussian distribution
    mu, std = np.mean(data), np.std(data)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = np.exp(-0.5 * ((x - mu) / std) ** 2) / (std * np.sqrt(2 * np.pi))
    
    plt.subplot(2, 2, 2)
    plt.plot(x, p, 'k', linewidth=2, label='Gaussian Distribution')
    plt.title('Gaussian Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    
    # Frequency smoothened KDE plot
    plt.subplot(2, 2, 3)
    sns.kdeplot(data, bw_adjust=0.5, fill=True)
    plt.title('Frequency Smoothened KDE Plot')
    plt.xlabel('Value')
    plt.ylabel('Density')

    # Gaussian distribution & smoothened KDE plot
    plt.subplot(2, 2, 4)
    sns.kdeplot(data, bw_adjust=0.5, label='KDE', color='orange')
    plt.plot(x, p, 'k', linewidth=2, label='Gaussian Distribution')
    plt.title('Gaussian Distribution & Smoothened KDE Plot')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()

    plt.tight_layout()
    plt.show()

visualize_data(int_list2)

# (ii) Function to calculate the range of a list of numbers
def calculate_range(data):
    return np.max(data) - np.min(data)

# (iii) Function to find variance and standard deviation
def variance_and_std(data):
    variance = np.var(data)
    std_deviation = np.std(data)
    return variance, std_deviation

# (iv) Function to compute the interquartile range (IQR)
def interquartile_range(data):
    q75, q25 = np.percentile(data, [75 ,25])
    return q75 - q25

# (v) Function to calculate coefficient of variation
def coefficient_of_variation(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    return std_dev / mean

# (vi) Function to find the mean absolute deviation (MAD)
def mean_absolute_deviation(data):
    mean = np.mean(data)
    return np.mean(np.abs(data - mean))

# (vii) Function to calculate the quartile deviation
def quartile_deviation(data):
    q75, q25 = np.percentile(data, [75 ,25])
    return (q75 - q25) / 2

# (viii) Function to find range-based coefficient of dispersion
def range_coefficient_of_dispersion(data):
    return (np.std(data) / (np.max(data) - np.min(data)))

# Example usage of the functions
if __name__ == "__main__":
    print("Generated List:", int_list2[:10], "...")  # Display the first 10 numbers

    # (ii)
    data_range = calculate_range(int_list2)
    print("Range of the list:", data_range)

    # (iii)
    variance, std_deviation = variance_and_std(int_list2)
    print("Variance:", variance)
    print("Standard Deviation:", std_deviation)

    # (iv)
    iqr = interquartile_range(int_list2)
    print("Interquartile Range (IQR):", iqr)

    # (v)
    cv = coefficient_of_variation(int_list2)
    print("Coefficient of Variation:", cv)

    # (vi)
    mad = mean_absolute_deviation(int_list2)
    print("Mean Absolute Deviation (MAD):", mad)

    # (vii)
    quartile_dev = quartile_deviation(int_list2)
    print("Quartile Deviation:", quartile_dev)

    # (viii)
    range_cv = range_coefficient_of_dispersion(int_list2)
    print("Range-based Coefficient of Dispersion:", range_cv)
