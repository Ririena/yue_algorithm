import itertools
import math

data = ["A","B", "C", "D", "e"]
permutation = itertools.permutations(data)
length_of_perm = 0
length_of_comb = 0
for perm in permutation:
    length_of_perm += 1
    print(f"Data {perm}")

combination = itertools.combinations(data, 3)

for comb in combination:
    length_of_comb += 1
    print(comb)

print(5*4*3*2*1)

combination_form = (math.factorial(5)) / (math.factorial(5) - math.factorial(3))

print(length_of_perm)
print(length_of_comb)
print(combination_form)
