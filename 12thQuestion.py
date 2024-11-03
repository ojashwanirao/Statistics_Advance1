#12.A tutoring service claims that its program improves students' exam scores. A sample of students who participated in the program was taken, and their scores before and after the program were recorded.

#Use the below code to generate samples of respective arrays of marks:
#```python
#before_program = np.array([75, 80, 85, 70, 90, 78, 92, 88, 82, 87])
#after_program = np.array([80, 85, 90, 80, 92, 80, 95, 90, 85, 88]
#```
#Use z-test to find if the claims made by tutor are true or false.

import numpy as np
from scipy.stats import norm

# Scores before and after the tutoring program
before_program = np.array([75, 80, 85, 70, 90, 78, 92, 88, 82, 87])
after_program = np.array([80, 85, 90, 80, 92, 80, 95, 90, 85, 88])

# Calculate the differences
differences = after_program - before_program

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
    print("Result: The tutoring program is effective in improving exam scores.")
else:
    print("Result: The tutoring program does not significantly improve exam scores.")
