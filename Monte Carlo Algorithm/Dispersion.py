# ======================================================
# Material Component: Dispersions
# Objective: Learn Range, Variance, Standard Deviation, Interquartile Range
# Language: Python
# ======================================================

import numpy as np
import statistics as st
import random as rd
import math

from numpy.ma.extras import average

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

#Variance

data_one = [2,3,4,5,6,7]
average_data_one = np.mean(data_one)

print(f"Average of Data One: {average_data_one}")

average_1 = (2-average_data_one) ** 2
average_2 = (3-average_data_one) ** 2
average_3 = (4-average_data_one) ** 2
average_4 = (5-average_data_one) ** 2
average_5 = (6-average_data_one) ** 2
average_6 = (7-average_data_one) ** 2



variance = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6) / 6
print(variance)
root = math.sqrt(variance)
print(root)

list_data = []


for data in data_one:
    calculated = (data - average_data_one) ** 2
    list_data.append(float(calculated))
    summation = sum(list_data)
    print(f"Summation {summation}")
    variance_population = summation / len(data_one)
    variance_sampel = summation / 5


print(f" Adalah {list_data}")
print(f" Variansi Populasinya {variance_population}")
print(f" Variansi Sampelnya {variance_sampel}")
standar_deviasi = math.sqrt(variance_population)
print(f"Standar Deviasi {standar_deviasi}")

square_root = math.sqrt(50)
print(square_root)

