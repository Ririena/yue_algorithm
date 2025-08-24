# ======================================================
# Material Component: Dispersions
# Objective: Learn Range, Variance, Standard Deviation, Interquartile Range
# Language: Python
# ======================================================

import numpy as np
import statistics as st
import random as rd

# ======================================================
# Example Dataset
# ======================================================
some_data = [20, 40, 16, 32, 39, 21]

# ======================================================
# Calculate Range
# ======================================================
# Range is the spread of data from the lowest to the highest value in the dataset
# Formula: Range = Max - Min

data_max = np.max(some_data)  # Find the maximum value
data_min = np.min(some_data)  # Find the minimum value

print(f"Data Max: {data_max}")
print(f"Data Min: {data_min}")

data_range = data_max - data_min  # Calculate the range
print(f"Data Range Calculation: {data_range}")

# Interpretation:
# If the range is low → the data is consistent (values are close to each other)
# If the range is high → the data is spread out / dispersed (values vary widely)

# ======================================================
# Analogy: Rolling D&D dice for healing
# ======================================================
# Simulate rolling 8d6 (8 rolls of a 6-sided dice)
result = []

for roll_8d6 in range(8):
    calculate = rd.randint(1, 6)  # Random number between 1 and 6
    result.append(calculate)

total = sum(result)  # Sum of all rolls
print(f"The Result of Healings {result}: {total}")

# Observation:
# The data is relatively consistent, ranging roughly from 21 to 48,
# not too far from the expected mean.

# Now, let's simulate rolling 6d8 (6 rolls of an 8-sided dice)
result_1 = []

for roll_6d8 in range(6):
    calculate = rd.randint(1, 8)  # Random number between 1 and 8
    result_1.append(calculate)

total_1 = sum(result_1)  # Sum of all rolls
print(f"The Result of Healings {result_1}: {total_1}")

# Interpretation:
# Similar principle applies: total will vary within the possible min and max,
# showing how dice rolls can illustrate the concept of data range and dispersion.
