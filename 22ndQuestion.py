#22. A company conducted a customer satisfaction survey to determine if there is a significant relationship between product satisfaction levels (Satisfied, Neutral, Dissatisfied) and the region where customers are located (East, West, North, South). The survey data is summarized in a contingency table. Conduct a ChiSquare test to determine if there is a significant relationship between product satisfaction levels and customer regions.

#Sample data:
#```python
#Sample data: Product satisfaction levels (rows) vs. Customer regions (columns)
#data = np.array([[50, 30, 40, 20], [30, 40, 30, 50], [20, 30, 40, 30]])
#```

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# Sample data: Product satisfaction levels (rows) vs. Customer regions (columns)
data = np.array([[50, 30, 40, 20],  # Satisfied
                 [30, 40, 30, 50],  # Neutral
                 [20, 30, 40, 30]])  # Dissatisfied

# Create a DataFrame for better visualization
satisfaction_levels = ['Satisfied', 'Neutral', 'Dissatisfied']
regions = ['East', 'West', 'North', 'South']
contingency_table = pd.DataFrame(data, index=satisfaction_levels, columns=regions)

# Display the contingency table
print("Contingency Table:")
print(contingency_table)

# Perform Chi-Square test
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

# Print results
print(f"\nChi-Square Statistic: {chi2_stat:.4f}")
print(f"P-Value: {p_value:.4f}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("There is a significant relationship between product satisfaction levels and customer regions.")
else:
    print("There is no significant relationship between product satisfaction levels and customer regions.")
