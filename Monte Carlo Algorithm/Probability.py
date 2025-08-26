# ======================================================
# Material Component: Probability
# Objective: Sample Point, Sample Space
# Language: Python
# ======================================================

import random as rn
import numpy as np

# Probability is the likelihood of an event occurring.
# Its value is always between 0 (impossible) and 1 (certain to occur)

# Basic Formula of Probability
# P(A) = total event A that desired / Total many possibility
# e.g i will talk about dice, one dice has 6 side that mean 6 possibility and total event that desire is the
# value that we wanted so we can calculate it like this so even we want a number but the possibility is 6
# the desired dice always one

desired_dice = 1
dice_side = 6
basic_possiblity = desired_dice / dice_side

print(f"{basic_possiblity * 100}%")

# Alright i move that part, so there is Sample Space, Sample Space is the values that unique i can say like in dice
# is like values of 1,2,3 .. 6 like that, it called sample Space
# Move to last one, this things called Sample Point or we can say the member of Sample Space it called Sample Point
# example in one dice theres 6 side okay, every side that we roll is called Sample Point so example i rolled dice
# an i got 4 that mean the sample point i got is 4

# furthermore to be clearly, example i rolled 2 dice, remember one dice has 6 sample that mean if 2 dice we had 36
# example i rolled dice 2 and i got {1,4} if we pull the string it many from {1,1} to .. {6,6}

# case if we roll 2 dice and how to find sample point

dice_1 = []
dice_2 = []
desired_dices = 1
dice_side = 6
all_combinations = []

for d1 in range(1, dice_side + 1):
    for d2 in range(1, dice_side + 1):
        print((d1, d2))
        all_combinations.append((d1, d2))


length_data = len(all_combinations)
print(length_data)

# Complement Probability
# Formula = P(A^c) = 1 - P(A)
# One Dice has 6 side, example we want 3 as the desired number so we can write like this

p_sample_space = 6
p_sample_point = 6
p_complement = 1 # Desired Values one

calc_complement = 1 - (p_complement / p_sample_space)
print(calc_complement * 100)


