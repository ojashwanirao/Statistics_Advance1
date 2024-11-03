#13.A pharmaceutical company wants to determine if a new drug is effective in reducing blood pressure. They conduct a study and record blood pressure measurements before and after administering the drug.

#Use the below code to generate samples of respective arrays of blood pressure:
#```python
#before_drug = np.array([145, 150, 140, 135, 155, 160, 152, 148, 130, 138])
#after_drug = np.array([130, 140, 132, 128, 145, 148, 138, 136, 125, 130])
#```
#Implement z-test to find if the drug really works or not.

import numpy as np
from scipy.stats import norm

# Blood pressure measurements before and after administering the drug
before_drug = np.array([145, 150, 140, 135, 155, 160, 152, 148, 130, 138])
after_drug = np.array([130, 140, 132, 128, 145, 148, 138, 136, 125, 130])

# Calculate the differences
differences = before_drug - after_drug

# Mean and standard deviation of the differences
mean_diff = np.mean(differences)
std_diff = np.std(differences, ddof=1)  # Sample standard deviation
n = len(differences)

# Calculate the z-score
z_score = mean_diff / (std_diff / np.sqrt(n))

# Determine the p-value for the one-tailed test
p_value = 1 - norm.cdf(z_score)

# Significance level
alpha = 0.05

# Output the results
print("Mean of Differences:", mean_diff)
print("Z-Score:", z_score)
print("p-value:", p_value)

# Conclusion
if p_value < alpha:
    print("Result: The drug is effective in reducing blood pressure.")
else:
    print("Result: The drug does not have a significant effect on blood pressure.")