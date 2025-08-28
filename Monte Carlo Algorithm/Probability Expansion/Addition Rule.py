# ======================================================
#  Material Test: Complement Probability
#  Objective: To Simulate The Addition Rule in Probability
#  Language: Python
# ======================================================

dice = [1, 2, 3, 4, 5, 6]

# Event Non Mutually Exclusive or has Intersection between 2 events
event1 = [d for d in dice if d % 2 == 1]  # ganjil
event2 = [d for d in dice if d < 3]  # kurang dari 3

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

calculate = (3 / 6) + (2 / 6) - 1 / 6

print(1 / 2 + 1 / 3)

# Mutually Exclusive
# e.g, how many ACE and Hearth of 4
ME1 = 4  # ACE IN CARD
ME2 = 1  # 4 Hearth is one

calculate_me = (ME1 / 52) + (ME2 / 52)
print(calculate_me)

# Daftar suits dan ranks
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Buat array semua kartu
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

# Cetak deck
print(deck)
print(f"Total cards: {len(deck)}")

# How Many Heart and 2-10 Number
# Non Mutually Exclusive

hearth = 13
number_card = 10

# Hardcode Number
number_h = ["aoh", "JH", "KH", "QH", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h"]
number_s = ["aos", "JS", "KS", "QS", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "10s"]
number_d = ["aod", "JD", "KD", "QD", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "10d"]
number_c = ["aoc", "JC", "KC", "QC", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c"]

merge_number = number_h + number_s + number_d + number_c
sample_space_card = len(merge_number)
print(merge_number)
print(f"Total Sample of Card {sample_space_card}")

events1 = [card for card in merge_number if card.lower().endswith('h')]
numbers = [card for card in merge_number if card[0] in "2345678910"]

intersect = [card for card in events1 if card in numbers]
print(len(events1))
print(len(numbers))

PEA = len(event1) / sample_space_card
PEB = len(numbers) / sample_space_card
P_intersect = len(intersect) / sample_space_card

print(P_intersect)

PEA_OR_B = PEA + PEB - P_intersect
print(PEA_OR_B)

EVENT1 = [card for card in merge_number if card.lower().endswith('h')]
EVENT2 = [card for card in merge_number if card[0] in("JKQ")]
EVENTI_INTERSECTION =  [card for card in EVENT1 if card in EVENT2]
print(EVENT2)

LENGTH_OF_HEARTH = len(EVENT1) / sample_space_card
LENGTH_OF_JQK = len(EVENT2) / sample_space_card
LENGTH_OF_IS = len(EVENTI_INTERSECTION) / sample_space_card

CALC_EV1_EV2 = (LENGTH_OF_HEARTH + LENGTH_OF_JQK) - LENGTH_OF_IS
print(CALC_EV1_EV2)

# TEST 4 DAILY ACTIVITES

SISWA_SAMPLE = 100
SISWA_BASKET = 40
SISWA_VOLI = 30
SISWA_BOTH = 10

CALCULATE_SISWA = (SISWA_BASKET / SISWA_SAMPLE) + (SISWA_VOLI / SISWA_SAMPLE) - (SISWA_BOTH / SISWA_SAMPLE)
print(CALCULATE_SISWA)

# DICE = [1,2,3,4,5,6]
#
# EVENT_D_1 = [dices for dices in DICE if dices == 7]
# print(EVENT_D_1)

# TEST 3 COLOR BALL
RED_BALL = 5
BLUE_BALL = 4
YELLOW_BALL = 3
SAMPLE_SPACE_BALL = RED_BALL + BLUE_BALL + YELLOW_BALL

