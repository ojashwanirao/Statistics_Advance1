#3. Write a Python class representing a discrete random variable with methods to calculate its expected value and variance.

class DiscreteRandomVariable:
    def __init__(self, probabilities, values):
        """
        Initialize the discrete random variable.

        Parameters:
        probabilities (list): A list of probabilities corresponding to each value.
        values (list): A list of values of the discrete random variable.
        """
        if len(probabilities) != len(values):
            raise ValueError("The length of probabilities and values must be the same.")
        if not all(0 <= p <= 1 for p in probabilities) or not (sum(probabilities) == 1):
            raise ValueError("Probabilities must be in the range [0, 1] and sum to 1.")

        self.probabilities = probabilities
        self.values = values

    def expected_value(self):
        """Calculate the expected value of the discrete random variable."""
        return sum(p * x for p, x in zip(self.probabilities, self.values))

    def variance(self):
        """Calculate the variance of the discrete random variable."""
        mean = self.expected_value()
        return sum(p * (x - mean) ** 2 for p, x in zip(self.probabilities, self.values))

# Example usage
if __name__ == "__main__":
    # Define the probabilities and values for the discrete random variable
    probabilities = [0.2, 0.5, 0.3]  # Probabilities must sum to 1
    values = [1, 2, 3]

    # Create an instance of DiscreteRandomVariable
    random_variable = DiscreteRandomVariable(probabilities, values)

    # Calculate and display expected value and variance
    print("Expected Value:", random_variable.expected_value())
    print("Variance:", random_variable.variance())
