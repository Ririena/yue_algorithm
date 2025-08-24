# ======================================================
# Materal Component: Statistics Basics
# Objective: Learn Statistics Basics Like, Max, Min, Mean, Mode etc
# Language: Python
# ======================================================

# numpy is python library exclusively facilitate array things and advanced mathematics
import numpy as np
import statistics as st
# Max, is a function to find the maximum value in one data
# example

some_data = [70, 50, 40, 20, 60, 20, 90]
calculate_max = np.max(some_data)
print(calculate_max) #90

# on the other hand there is a min function like the opposite of max

calculate_min = np.min(some_data)
print(calculate_min) #20

#Mean is the average value on some data
calculate_mean = np.mean(some_data)
print(calculate_mean) #55

# Mode or the values that appear most frequently on some data
calculate_mode = st.mode(some_data)
print(calculate_mode) #20



