# ======================================================
# Material Component: Probability
# Objective: To Compare Probability and Freequency
# Language: Python
# ======================================================
from random import sample

# Basic Formula of Probability is


# Input jumlah percobaan
trials = int(input("How many trials do you want to simulate? "))

# Probabilitas teoretis (dadu fair → peluang angka 6)
probability = 1/6
desired_value = 1
dice_side = 6

sample_point = dice_side ** trials

teoritical_prob = desired_value / sample_point

print(sample_point)

# Frekuensi harapan (berapa kali angka 6 seharusnya muncul)
expected_frequency = trials * probability

# Output
print(f"Probability Theoretic: {probability*100:.2f}%")
print(f"Expected Frequency for {trials} trials: {expected_frequency:.0f} times")


