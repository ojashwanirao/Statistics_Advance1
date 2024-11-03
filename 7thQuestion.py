#7. Use seaborn library to load tips dataset. Find the following from the dataset for the columns total_bill and tip`:

#(i) Write a Python function that calculates their skewness.
#(ii) Create a program that determines whether the columns exhibit positive skewness, negative skewness, or is approximately symmetric.
#(iii) Write a function that calculates the covariance between two columns.
#(iv) Implement a Python program that calculates the Pearson correlation coefficient between two columns.
#(v) Write a script to visualize the correlation between two specific columns in a Pandas DataFrame using scatter plots.

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, pearsonr

# Load the tips dataset
tips = sns.load_dataset("tips")

# (i) Function to calculate skewness
def calculate_skewness(column):
    return skew(column)

# (ii) Function to determine skewness type
def skewness_type(column):
    skewness = calculate_skewness(column)
    if skewness > 0:
        return "Positive Skewness"
    elif skewness < 0:
        return "Negative Skewness"
    else:
        return "Approximately Symmetric"

# (iii) Function to calculate covariance
def calculate_covariance(col1, col2):
    return np.cov(col1, col2)[0][1]

# (iv) Function to calculate Pearson correlation coefficient
def calculate_pearson_correlation(col1, col2):
    correlation, _ = pearsonr(col1, col2)
    return correlation

# (v) Function to visualize correlation with scatter plot
def visualize_correlation(df, col1, col2):
    plt.figure(figsize=(8, 6))
    plt.scatter(df[col1], df[col2], alpha=0.5)
    plt.title(f'Scatter Plot of {col1} vs {col2}')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.grid(True)
    plt.show()

# Analyze total_bill and tip columns
total_bill = tips['total_bill']
tip = tips['tip']

# Calculate skewness
total_bill_skewness = calculate_skewness(total_bill)
tip_skewness = calculate_skewness(tip)

# Determine skewness type
total_bill_skewness_type = skewness_type(total_bill)
tip_skewness_type = skewness_type(tip)

# Calculate covariance
covariance = calculate_covariance(total_bill, tip)

# Calculate Pearson correlation coefficient
pearson_correlation = calculate_pearson_correlation(total_bill, tip)

# Output the results
print(f"Total Bill Skewness: {total_bill_skewness} - {total_bill_skewness_type}")
print(f"Tip Skewness: {tip_skewness} - {tip_skewness_type}")
print(f"Covariance between total_bill and tip: {covariance}")
print(f"Pearson Correlation Coefficient between total_bill and tip: {pearson_correlation}")

# Visualize correlation
visualize_correlation(tips, 'total_bill', 'tip')
