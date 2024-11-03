#19. A manufacturer produces two different versions of a product and wants to compare their quality scores. Create a Python function to analyze quality assessment data, calculate the t-statistic, and decid whether there's a significant difference in quality between the two versions.

#Use the following data:
#```python
#version1_scores = [85, 88, 82, 89, 87, 84, 90, 88, 85, 86, 91, 83, 87, 84, 89, 86, 84, 88, 85, 86, 89, 90, 87, 88, 85]
#version2_scores = [80, 78, 83, 81, 79, 82, 76, 80, 78, 81, 77, 82, 80, 79, 82, 79, 80, 81, 79, 82, 79, 78, 80, 81, 82]
#`''

import numpy as np
from scipy import stats

# Quality assessment data for both versions
version1_scores = [85, 88, 82, 89, 87, 84, 90, 88, 85, 86, 91, 83, 87, 84, 89, 86, 84, 88, 85, 86, 89, 90, 87, 88, 85]
version2_scores = [80, 78, 83, 81, 79, 82, 76, 80, 78, 81, 77, 82, 80, 79, 82, 79, 80, 81, 79, 82, 79, 78, 80, 81, 82]

def analyze_quality_scores(version1_scores, version2_scores):
    # Calculate means
    mean_version1 = np.mean(version1_scores)
    mean_version2 = np.mean(version2_scores)

    # Calculate standard deviations
    std_version1 = np.std(version1_scores, ddof=1)  # Sample standard deviation
    std_version2 = np.std(version2_scores, ddof=1)  # Sample standard deviation

    # Sample sizes
    n_version1 = len(version1_scores)
    n_version2 = len(version2_scores)

    # Calculate t-statistic
    t_statistic = (mean_version1 - mean_version2) / np.sqrt((std_version1**2 / n_version1) + (std_version2**2 / n_version2))

    # Calculate degrees of freedom
    df = n_version1 + n_version2 - 2

    # Calculate p-value for two-tailed test
    p_value = stats.t.sf(np.abs(t_statistic), df) * 2  # two-tailed test

    return t_statistic, df, p_value, mean_version1, mean_version2

# Perform the analysis
t_stat, degrees_of_freedom, p_val, mean_version1, mean_version2 = analyze_quality_scores(version1_scores, version2_scores)

# Print results
print(f"Version 1 Scores (Mean): {mean_version1:.2f}, Standard Deviation: {np.std(version1_scores, ddof=1):.2f}")
print(f"Version 2 Scores (Mean): {mean_version2:.2f}, Standard Deviation: {np.std(version2_scores, ddof=1):.2f}")
print(f"T-statistic: {t_stat:.4f}")
print(f"Degrees of Freedom: {degrees_of_freedom}")
print(f"P-value: {p_val:.4f}")

# Interpretation
alpha = 0.05
if p_val < alpha:
    print("There is a statistically significant difference in quality between the two product versions.")
else:
    print("There is no statistically significant difference in quality between the two product versions.")
