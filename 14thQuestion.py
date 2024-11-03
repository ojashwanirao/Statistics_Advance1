#14. A customer service department claims that their average response time is less than 5 minutes. A sample of recent customer interactions was taken, and the response times were recorded.

#Implement the below code to generate the array of response time:
#```python
#response_times = np.array([4.3, 3.8, 5.1, 4.9, 4.7, 4.2, 5.2, 4.5, 4.6, 4.4])
#```
#Implement z-test to find the claims made by customer service department are tru or false.

import numpy as np
from scipy.stats import norm

# Response times sample data
response_times = np.array([4.3, 3.8, 5.1, 4.9, 4.7, 4.2, 5.2, 4.5, 4.6, 4.4])

# Hypothesized population mean
mu = 5

# Sample mean and sample standard deviation
sample_mean = np.mean(response_times)
sample_std = np.std(response_times, ddof=1)  # Use ddof=1 for sample standard deviation
n = len(response_times)

# Calculate the z-score
z_score = (sample_mean - mu) / (sample_std / np.sqrt(n))

# Determine the p-value for the one-tailed test
p_value = norm.cdf(z_score)

# Significance level
alpha = 0.05

# Output the results
print("Sample Mean:", sample_mean)
print("Z-Score:", z_score)
print("p-value:", p_value)

# Conclusion
if p_value < alpha:
    print("Result: The claim is true. Average response time is significantly less than 5 minutes.")
else:
    print("Result: The claim is not supported. Average response time is not significantly less than 5 minutes.")

