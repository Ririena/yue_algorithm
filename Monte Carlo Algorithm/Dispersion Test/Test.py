import random as rn
import numpy as np
import math

total_data = []
for i in range(1,7):
    generate_number = rn.randint(20,46)
    total_data.append(generate_number)

print(total_data)

length_data = len(total_data)
print(f"Panjang Data: {length_data}")

mean_data = np.mean(total_data)
print(f"Average Data: {mean_data}")

squared_differences = []
for data in total_data:
    calculated = (data - mean_data) ** 2
    squared_differences.append(float(calculated))

summation = sum(squared_differences)
print(f"Total Jumlah: {summation}")

population_variation = summation / length_data
sample_variation = summation / (length_data - 1)
standard_deviation = math.sqrt(population_variation)

print(f"Populasi Variasi nya: {population_variation}")
print(f"Sample Variasi nya: {sample_variation}")
print(f"Standard Deviasi nya: {standard_deviation}")




