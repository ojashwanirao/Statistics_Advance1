#24. A company produces three different versions of a product: Standard, Premium, and Deluxe. The company wants to determine if there is a significant difference in customer satisfaction scores among the three product versions. They conducted a survey and collected customer satisfaction scores for each version from a random sample of customers. Perform an ANOVA test to determine if there is a significant difference in customer satisfaction scores.

#Use the following data:
#```python
#Sample data: Customer satisfaction scores for each product version
#standard_scores = [80, 85, 90, 78, 88, 82, 92, 78, 85, 87]
#premium_scores = [90, 92, 88, 92, 95, 91, 96, 93, 89, 93]
#deluxe_scores = [95, 98, 92, 97, 96, 94, 98, 97, 92, 99]

import numpy as np
import pandas as pd
from scipy.stats import f_oneway

# Sample data: Customer satisfaction scores for each product version
standard_scores = [80, 85, 90, 78, 88, 82, 92, 78, 85, 87]
premium_scores = [90, 92, 88, 92, 95, 91, 96, 93, 89, 93]
deluxe_scores = [95, 98, 92, 97, 96, 94, 98, 97, 92, 99]

# Perform ANOVA test
f_statistic, p_value = f_oneway(standard_scores, premium_scores, deluxe_scores)

# Print results
print(f"F-Statistic: {f_statistic:.4f}")
print(f"P-Value: {p_value:.4f}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("There is a significant difference in customer satisfaction scores among the product versions.")
else:
    print("There is no significant difference in customer satisfaction scores among the product versions.")