#11. A company wants to test if a new website layout leads to a higher conversion rate (percentage of visitors who make a purchase). They collect data from the old and new layouts to compare.

#To generate the data use the following command:
#```python
#import numpy as np
# 50 purchases out of 1000 visitors
#old_layout = np.array([1] * 50 + [0] * 950)
# 70 purchases out of 1000 visitors  
#new_layout = np.array([1] * 70 + [0] * 930)
#```
#Apply z-test to find which layout is successful.

import numpy as np
from scipy.stats import norm

# Data for old and new layouts
old_layout = np.array([1] * 50 + [0] * 950)
new_layout = np.array([1] * 70 + [0] * 930)

# Calculate conversion rates
p_old = np.mean(old_layout)
p_new = np.mean(new_layout)

# Pooled conversion rate
p_pooled = (p_old * len(old_layout) + p_new * len(new_layout)) / (len(old_layout) + len(new_layout))

# Standard error
se = np.sqrt(p_pooled * (1 - p_pooled) * (1/len(old_layout) + 1/len(new_layout)))

# Calculate z-score
z_score = (p_new - p_old) / se

# Determine p-value for one-tailed test
p_value = 1 - norm.cdf(z_score)

# Significance level
alpha = 0.05

# Output results
print("Old Layout Conversion Rate:", p_old)
print("New Layout Conversion Rate:", p_new)
print("Z-Score:", z_score)
print("p-value:", p_value)

# Conclusion
if p_value < alpha:
    print("Result: The new layout has a significantly higher conversion rate.")
else:
    print("Result: There is no significant difference in conversion rates between layouts.")
