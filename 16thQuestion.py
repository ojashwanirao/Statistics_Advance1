#16. A pharmaceutical company wants to determine if a new drug is more effective than an existing drug in reducing cholesterol levels. Create a program to analyze the clinical trial data and calculate the tstatistic and p-value for the treatment effect.


#Use the following data of cholestrol level:
#```python
#existing_drug_levels = [180, 182, 175, 185, 178, 176, 172, 184, 179, 183]
#new_drug_levels = [170, 172, 165, 168, 175, 173, 170, 178, 172, 176]
#```

import numpy as np
from scipy import stats

def compare_drugs(existing_drug_levels, new_drug_levels):
    # Calculate means
    mean_existing = np.mean(existing_drug_levels)
    mean_new = np.mean(new_drug_levels)

    # Calculate standard deviations
    std_existing = np.std(existing_drug_levels, ddof=1)  # Sample standard deviation
    std_new = np.std(new_drug_levels, ddof=1)  # Sample standard deviation

    # Sample sizes
    n_existing = len(existing_drug_levels)
    n_new = len(new_drug_levels)

    # Calculate t-statistic
    t_statistic = (mean_new - mean_existing) / np.sqrt((std_existing**2 / n_existing) + (std_new**2 / n_new))

    # Calculate degrees of freedom
    df = n_existing + n_new - 2

    # Calculate p-value for two-tailed test
    p_value = stats.t.sf(np.abs(t_statistic), df) * 2  # two-tailed test

    return t_statistic, df, p_value

# Provided data
existing_drug_levels = [180, 182, 175, 185, 178, 176, 172, 184, 179, 183]
new_drug_levels = [170, 172, 165, 168, 175, 173, 170, 178, 172, 176]

# Perform the comparison
t_stat, degrees_of_freedom, p_val = compare_drugs(existing_drug_levels, new_drug_levels)

# Print results
print(f"T-statistic: {t_stat:.4f}")
print(f"Degrees of Freedom: {degrees_of_freedom}")
print(f"P-value: {p_val:.4f}")

# Interpretation
alpha = 0.05
if p_val < alpha:
    print("The new drug is significantly more effective in reducing cholesterol levels compared to the existing drug.")
else:
    print("There is no significant difference in effectiveness between the new drug and the existing drug.")
