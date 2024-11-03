#20. A restaurant chain collects customer satisfaction scores for two different branches. Write a program to analyze the scores, calculate the t-statistic, and determine if there's a statistically significant difference in customer satisfaction between the branches.

#Use the below data of scores:
#  ```python
#branch_a_scores = [4, 5, 3, 4, 5, 4, 5, 3, 4, 4, 5, 4, 4, 3, 4, 5, 5, 4, 3, 4, 5, 4, 3, 5, 4, 4, 5, 3, 4, 5, 4]
#branch_b_scores = [3, 4, 2, 3, 4, 3, 4, 2, 3, 3, 4, 3, 3, 2, 3, 4, 4, 3, 2, 3, 4, 3, 2, 4, 3, 3, 4, 2, 3, 4, 3]

import numpy as np
from scipy import stats

# Customer satisfaction scores for both branches
branch_a_scores = [4, 5, 3, 4, 5, 4, 5, 3, 4, 4, 5, 4, 4, 3, 4, 5, 5, 4, 3, 4, 5, 4, 3, 5, 4, 4, 5, 3, 4, 5, 4]
branch_b_scores = [3, 4, 2, 3, 4, 3, 4, 2, 3, 3, 4, 3, 3, 2, 3, 4, 4, 3, 2, 3, 4, 3, 2, 4, 3, 3, 4, 2, 3, 4, 3]

def analyze_satisfaction_scores(branch_a_scores, branch_b_scores):
    # Calculate means
    mean_branch_a = np.mean(branch_a_scores)
    mean_branch_b = np.mean(branch_b_scores)

    # Calculate standard deviations
    std_branch_a = np.std(branch_a_scores, ddof=1)  # Sample standard deviation
    std_branch_b = np.std(branch_b_scores, ddof=1)  # Sample standard deviation

    # Sample sizes
    n_branch_a = len(branch_a_scores)
    n_branch_b = len(branch_b_scores)

    # Calculate t-statistic
    t_statistic = (mean_branch_a - mean_branch_b) / np.sqrt((std_branch_a**2 / n_branch_a) + (std_branch_b**2 / n_branch_b))

    # Calculate degrees of freedom
    df = n_branch_a + n_branch_b - 2

    # Calculate p-value for two-tailed test
    p_value = stats.t.sf(np.abs(t_statistic), df) * 2  # two-tailed test

    return t_statistic, df, p_value, mean_branch_a, mean_branch_b

# Perform the analysis
t_stat, degrees_of_freedom, p_val, mean_branch_a, mean_branch_b = analyze_satisfaction_scores(branch_a_scores, branch_b_scores)

# Print results
print(f"Branch A Scores (Mean): {mean_branch_a:.2f}, Standard Deviation: {np.std(branch_a_scores, ddof=1):.2f}")
print(f"Branch B Scores (Mean): {mean_branch_b:.2f}, Standard Deviation: {np.std(branch_b_scores, ddof=1):.2f}")
print(f"T-statistic: {t_stat:.4f}")
print(f"Degrees of Freedom: {degrees_of_freedom}")
print(f"P-value: {p_val:.4f}")

# Interpretation
alpha = 0.05
if p_val < alpha:
    print("There is a statistically significant difference in customer satisfaction between the two branches.")
else:
    print("There is no statistically significant difference in customer satisfaction between the two branches.")
