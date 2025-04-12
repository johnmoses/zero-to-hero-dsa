"""
Finance Algorithm

Write a simple finance algorithm to
calculate the compound interest for a given principal amount, interest rate, and number of years.
"""

def compoundInterest(principal, rate, years):
    """
    Calculates the compound interest for a given principal amount, interest rate, and number of years.

    Args:
        principal (float): The principal amount.
        rate (float): The interest rate (in decimal form).
        years (int): The number of years.

    Returns:
        float: The compound interest.
    """
    # Calculate the compound interest using the formula: A = P(1 + r)^t
    return principal * (1 + rate) ** years

# Example usage
principal = 1000
rate = 0.05
years = 5
print(compoundInterest(principal, rate, years))  # Output: 1276.28
