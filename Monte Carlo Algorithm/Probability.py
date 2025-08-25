# ======================================================
# Material Component: Probability
# Objective: Sample Point, Sample Space
# Language: Python
# ======================================================

# Dice sample_space, each one dice has 6 side that mean the sample of one dice
# is 6

import random as rn
import numpy as np

trials = 2
probability_of_dice = 6
sample_space = probability_of_dice ** trials

print(sample_space)

# Sample Points
for i in range(1, probability_of_dice + 1):
    for j in range(1, probability_of_dice + 1):
        print((i,j))

print(sample_space)

trials = 3

#Probability of dice 5 appear
#
# trials = 3
# p_single = 1/6
#
# p_at_least_one_5 = 1 - (1 - p_single) ** trials
# p_two_5s = p_single ** trials
#
# print(p_at_least_one_5 * 100)
# print(p_two_5s * 100)
#
# trials_of_dice = 3
# p_single = 1/6
#
# p_at_least_one_5_and_3 = 2 * (p_single * p_single)
# print(p_at_least_one_5_and_3 * 100)
#
#

# Dice 6 can appear in 6 trials

probability_of_6 = 1/36
n = 3
expected_frequency = probability_of_6 * n
print("Frekuensi harapan (teori):", expected_frequency)
#
# rolled_dadu = []
# dadu_6 = []
#
# for _ in range(n):
#     roll = rn.randint(1, 6)       # lempar dadu
#     rolled_dadu.append(roll)      # simpan hasil
#     if roll == 6:
#         dadu_6.append(roll)       # simpan kalau hasil 6
#
# print("Hasil lemparan:", rolled_dadu)
# print("Jumlah 6 yang muncul:", len(dadu_6))

#
#
#
#

