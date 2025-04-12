""" 
Simple moving average
"""

from collections.abc import Sequence

def simple_moving_average(
    data: Sequence[float], window_size: int
) -> list[float | None]:
    if window_size < 1:
        raise ValueError("Window size must be a positive integer")

    sma: list[float | None] = []
    for i in range(len(data)):
        if i < window_size - 1:
            sma.append(None)  # SMA not available for early data points
        else:
            window = data[i - window_size + 1 : i + 1]
            sma_value = sum(window) / window_size
            sma.append(sma_value)
    return sma

# Example data (replace with your own time series data)
data = [10, 12, 15, 13, 14, 16, 18, 17, 19, 21]

# Specify the window size for the SMA
window_size = 3

# Calculate the Simple Moving Average
print(sma_values = simple_moving_average(data, window_size))