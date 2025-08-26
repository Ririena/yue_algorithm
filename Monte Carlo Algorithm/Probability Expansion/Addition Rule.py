dice = [1, 2, 3, 4, 5, 6]

# Event
event1 = [d for d in dice if d % 2 == 1]  # ganjil
event2 = [d for d in dice if d < 3]       # kurang dari 3

# Probabilitas masing-masing
P_A = len(event1) / len(dice)
P_B = len(event2) / len(dice)

# Probabilitas irisan (A ∩ B)
intersection = [d for d in dice if d in event1 and d in event2]
P_A_and_B = len(intersection) / len(dice)

# Probabilitas gabungan (not mutually exclusive)
P_A_or_B = P_A + P_B - P_A_and_B

print("Event1:", event1)
print("Event2:", event2)
print("Intersection:", intersection)
print("P(A or B) =", P_A_or_B)

calculate = (3 / 6) + (2 / 6) - 1/6

print(1/2 + 1/3)