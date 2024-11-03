#23. A company implemented an employee training program to improve job performance (Effective, Neutral, Ineffective). After the training, they collected data from a sample of employees and classified them based on their job performance before and after the training. Perform a Chi-Square test to determine if there is a significant difference between job performance levels before and after the training.

#Sample data:
#```python
# Sample data: Job performance levels before (rows) and after (columns) training
#data = np.array([[50, 30, 20], [30, 40, 30], [20, 30, 40]])
#```

import numpy as np
from scipy.stats import chi2_contingency

# Sample data: Job performance levels before (rows) and after (columns) training
data = np.array([[50, 30, 20], 
                 [30, 40, 30], 
                 [20, 30, 40]])

# Perform the Chi-Square test
chi2_stat, p_value, dof, expected = chi2_contingency(data)

# Display the results
print("Chi-Square Statistic:", chi2_stat)
print("p-value:", p_value)
print("Degrees of Freedom:", dof)
print("Expected Frequencies:\n", expected)

# Conclusion based on p-value
alpha = 0.05
if p_value < alpha:
    print("Result: Significant difference in job performance levels before and after training.")
else:
    print("Result: No significant difference in job performance levels before and after training.")
