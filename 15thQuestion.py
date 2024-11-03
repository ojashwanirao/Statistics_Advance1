#15. A company is testing two different website layouts to see which one leads to higher click-through rates. Write a Python function to perform an A/B test analysis, including calculating the t-statistic, degrees of freedom, and p-value.

#Use the following data:
#```python
#layout_a_clicks = [28, 32, 33, 29, 31, 34, 30, 35, 36, 37]
#layout_b_clicks = [40, 41, 38, 42, 39, 44, 43, 41, 45, 47]

import numpy as np
from scipy import stats

def ab_test_analysis(layout_a_clicks, layout_b_clicks):
    # Calculate means
    mean_a = np.mean(layout_a_clicks)
    mean_b = np.mean(layout_b_clicks)
    
    # Calculate standard deviations
    std_a = np.std(layout_a_clicks, ddof=1)  # Sample standard deviation
    std_b = np.std(layout_b_clicks, ddof=1)  # Sample standard deviation
    
    # Sample sizes
    n_a = len(layout_a_clicks)
    n_b = len(layout_b_clicks)

    # Calculate t-statistic
    t_statistic = (mean_a - mean_b) / np.sqrt((std_a**2 / n_a) + (std_b**2 / n_b))
    
    # Calculate degrees of freedom
    df = n_a + n_b - 2

    # Calculate p-value for two-tailed test
    p_value = stats.t.sf(np.abs(t_statistic), df) * 2  # two-tailed test

    return t_statistic, df, p_value

# Example data
layout_a_clicks = [28, 32, 33, 29, 31, 34, 30, 35, 36, 37]
layout_b_clicks = [40, 41, 38, 42, 39, 44, 43, 41, 45, 47]

# Perform the A/B test analysis
t_stat, degrees_of_freedom, p_val = ab_test_analysis(layout_a_clicks, layout_b_clicks)

# Print results
print(f"T-statistic: {t_stat:.4f}")
print(f"Degrees of Freedom: {degrees_of_freedom}")
print(f"P-value: {p_val:.4f}")

# Interpretation
alpha = 0.05
if p_val < alpha:
    print("There is a significant difference in click-through rates between the two layouts.")
else:
    print("There is no significant difference in click-through rates between the two layouts.")
