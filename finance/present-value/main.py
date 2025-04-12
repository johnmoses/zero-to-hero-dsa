""" 
An algorithm that calculates the present value of a stream of yearly cash flows given...
1. The discount rate (as a decimal, not a percent)
2. An array of cash flows, with the index of the cash flow being the associated year
"""

def present_value(discount_rate: float, cash_flows: list[float]) -> float:
    if discount_rate < 0:
        raise ValueError("Discount rate cannot be negative")
    if not cash_flows:
        raise ValueError("Cash flows list cannot be empty")
    present_value = sum(
        cash_flow / ((1 + discount_rate) ** i) for i, cash_flow in enumerate(cash_flows)
    )
    return round(present_value, ndigits=2)

print(present_value(0.07, [109129.39, 30923.23, 15098.93, 29734,39]))