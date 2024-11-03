#18. An HR department wants to investigate if there's a gender-based salary gap within the company. Developa program to analyze salary data, calculate the t-statistic, and determine if there's a statistically significant difference between the average salaries of male and female employees.

#Use the below code to generate synthetic data:
#```python
# Generate synthetic salary data for male and female employees
#np.random.seed(0)  # For reproducibility
#male_salaries = np.random.normal(loc=50000, scale=10000, size=20)
#female_salaries = np.random.normal(loc=55000, scale=9000, size=20)

import numpy as np
from scipy import stats

# Generate synthetic salary data for male and female employees
np.random.seed(0)  # For reproducibility
male_salaries = np.random.normal(loc=50000, scale=10000, size=20)
female_salaries = np.random.normal(loc=55000, scale=9000, size=20)

def analyze_salary_gap(male_salaries, female_salaries):
    # Calculate means
    mean_male = np.mean(male_salaries)
    mean_female = np.mean(female_salaries)

    # Calculate standard deviations
    std_male = np.std(male_salaries, ddof=1)  # Sample standard deviation
    std_female = np.std(female_salaries, ddof=1)  # Sample standard deviation

    # Sample sizes
    n_male = len(male_salaries)
    n_female = len(female_salaries)

    # Calculate t-statistic
    t_statistic = (mean_female - mean_male) / np.sqrt((std_male**2 / n_male) + (std_female**2 / n_female))

    # Calculate degrees of freedom
    df = n_male + n_female - 2

    # Calculate p-value for two-tailed test
    p_value = stats.t.sf(np.abs(t_statistic), df) * 2  # two-tailed test

    return t_statistic, df, p_value, mean_male, mean_female

# Perform the analysis
t_stat, degrees_of_freedom, p_val, mean_male, mean_female = analyze_salary_gap(male_salaries, female_salaries)

# Print results
print(f"Male Salaries (Mean): {mean_male:.2f}, Standard Deviation: {np.std(male_salaries, ddof=1):.2f}")
print(f"Female Salaries (Mean): {mean_female:.2f}, Standard Deviation: {np.std(female_salaries, ddof=1):.2f}")
print(f"T-statistic: {t_stat:.4f}")
print(f"Degrees of Freedom: {degrees_of_freedom}")
print(f"P-value: {p_val:.4f}")

# Interpretation
alpha = 0.05
if p_val < alpha:
    print("There is a statistically significant difference between the average salaries of male and female employees.")
else:
    print("There is no statistically significant difference between the average salaries of male and female employees.")
