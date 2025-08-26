import math
import random as rn

d_sample_space = 6
d_sample_point = 6
d_desire_values = 1 #4
roll = 1

p_not_4 =  1 - (d_desire_values / d_sample_space)

print(p_not_4 * 100)

c_sample_space = 2
c_sample_point = 2
c_desire_values = 1

c_not_head = 1 - (c_desire_values / c_sample_space)
print(c_not_head * 100)

d2_trials = 2
d2_side = 6
d2_sample_space = d2_side ** d2_trials
d2_desired_values = 1

d2_not_6 = 1 - (d2_desired_values / d2_sample_space)
print(d2_not_6 * 100)




