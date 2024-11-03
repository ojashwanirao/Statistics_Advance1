#21. A political analyst wants to determine if there is a significant association between age groups and voter preferences (Candidate A or Candidate B). They collect data from a sample of 500 voters and classify them into different age groups and candidate preferences. Perform a Chi-Square test to determine if there is a significant association between age groups and voter preferences.

#Use the below code to generate data:
#```python
#np.random.seed(0)
#age_groups = np.random.choice([ 18 30 , 31 50 , 51+', 51+'], size=30)
#voter_preferences = np.random.choice(['Candidate A', 'Candidate B'], size=30)

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# Set the random seed for reproducibility
np.random.seed(0)

# Generate synthetic data for age groups and voter preferences
age_groups = np.random.choice(['18-30', '31-50', '51+'], size=500)
voter_preferences = np.random.choice(['Candidate A', 'Candidate B'], size=500)

# Create a DataFrame
data = pd.DataFrame({
    'Age Group': age_groups,
    'Voter Preference': voter_preferences
})

# Create a contingency table
contingency_table = pd.crosstab(data['Age Group'], data['Voter Preference'])

# Perform Chi-Square test
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

# Print results
print("Contingency Table:")
print(contingency_table)
print(f"\nChi-Square Statistic: {chi2_stat:.4f}")
print(f"P-Value: {p_value:.4f}")
print(f"Degrees of Freedom: {dof}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("There is a significant association between age groups and voter preferences.")
else:
    print("There is no significant association between age groups and voter preferences.")
