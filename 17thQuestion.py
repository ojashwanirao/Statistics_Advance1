#17.A school district introduces an educational intervention program to improve math scores. Write a Python function to analyze pre- and post-intervention test scores, calculating the t-statistic and p-value to determine if the intervention had a significant impact.


#Use the following data of test score:
#```python
#pre_intervention_scores = [80, 85, 90, 75, 88, 82, 92, 78, 85, 87]
#post_intervention_scores = [90, 92, 88, 92, 95, 91, 96, 93, 89, 93]
#```

import numpy as np
from scipy import stats

def analyze_intervention(pre_scores, post_scores):
    # Calculate the differences between post and pre intervention scores
    differences = np.array(post_scores) - np.array(pre_scores)
    
    # Calculate the mean and standard deviation of the differences
    mean_diff = np.mean(differences)
    std_diff = np.std(differences, ddof=1)  # Sample standard deviation
    
    # Sample size
    n = len(differences)

    # Calculate t-statistic
    t_statistic = mean_diff / (std_diff / np.sqrt(n))

    # Calculate degrees of freedom
    df = n - 1

    # Calculate p-value for two-tailed test
    p_value = stats.t.sf(np.abs(t_statistic), df) * 2  # two-tailed test

    return t_statistic, df, p_value

# Provided test scores
pre_intervention_scores = [80, 85, 90, 75, 88, 82, 92, 78, 85, 87]
post_intervention_scores = [90, 92, 88, 92, 95, 91, 96, 93, 89, 93]

# Perform the analysis
t_stat, degrees_of_freedom, p_val = analyze_intervention(pre_intervention_scores, post_intervention_scores)

# Print results
print(f"T-statistic: {t_stat:.4f}")
print(f"Degrees of Freedom: {degrees_of_freedom}")
print(f"P-value: {p_val:.4f}")

# Interpretation
alpha = 0.05
if p_val < alpha:
    print("The educational intervention had a significant impact on math scores.")
else:
    print("The educational intervention did not have a significant impact on math scores.")
