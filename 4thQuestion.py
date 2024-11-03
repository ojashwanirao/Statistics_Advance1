#4. Implement a program to simulate the rolling of a fair six-sided die and calculate the expected value and variance of the outcomes.

import numpy as np

def simulate_die_rolls(num_rolls):
    """
    Simulate rolling a fair six-sided die.

    Parameters:
    num_rolls (int): The number of times to roll the die.

    Returns:
    np.ndarray: Array of outcomes from the die rolls.
    """
    outcomes = np.random.randint(1, 7, num_rolls)  # Rolls a die (1 to 6)
    return outcomes

def calculate_expected_value(outcomes):
    """
    Calculate the expected value of the outcomes.

    Parameters:
    outcomes (np.ndarray): Array of outcomes from the die rolls.

    Returns:
    float: Expected value of the outcomes.
    """
    return np.mean(outcomes)

def calculate_variance(outcomes):
    """
    Calculate the variance of the outcomes.

    Parameters:
    outcomes (np.ndarray): Array of outcomes from the die rolls.

    Returns:
    float: Variance of the outcomes.
    """
    return np.var(outcomes)

# Parameters
num_rolls = 1000  # Number of times to roll the die

# Simulate the die rolls
outcomes = simulate_die_rolls(num_rolls)

# Calculate expected value and variance
expected_value = calculate_expected_value(outcomes)
variance = calculate_variance(outcomes)

# Output the results
print(f"Outcomes from rolling the die: {outcomes}")
print(f"Expected Value: {expected_value}")
print(f"Variance: {variance}")
