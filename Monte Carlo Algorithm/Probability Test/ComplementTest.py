import random as rn
import numpy as np

# Test 1
default_side_dice = 6
default_dice_trials = 1
default_dice_sample = default_side_dice ** default_dice_trials


favorable_dice = 1
calculate_complement = 1 - (favorable_dice / default_dice_sample)
print(f"Kalkulasi Komplemen dadu yang bukan 5: {calculate_complement * 100}%")

# Test 2
default_side_coin = 2
default_coin_trials = 1
default_coin_sample = default_side_coin ** default_coin_trials
favorable_coin = 1

calculate_c_complement = 1 - (favorable_coin / default_coin_sample)
print(f"Kalkulasi komplemen coin yang bukan gambar: {calculate_c_complement * 100}%")

# Test 3
red_ball = 5
blue_ball = 3
default_ball_trials = 1
default_ball_sample = 8

calculate_ball_complement = 1 - (blue_ball / default_ball_sample)
print(f"Kalkulasi Komplemen bola yang bukan biru: {calculate_ball_complement * 100}%")

# Test 4

dadu_array = [1,2,3,4,5,6]
dadu_genap_data = []

for dadu_genap in dadu_array:
    if dadu_genap % 2 == 0:
        dadu_genap_data.append(dadu_genap)

length_genap = len(dadu_genap_data)

calculate_not_genap = 1 - (length_genap / default_dice_sample)
print(f"Kalkulasi dadu yang bukan genap: {calculate_not_genap * 100}%")

# Test 5
default_set_card = 52
default_set_as = 4

calculate_card_complement = 1 - (default_set_as / default_set_card)
print(f"Kalkulasi Tidak Mendapat AS adalah: {calculate_card_complement * 100}%")

# Test 6
length_of_dadu = 0
for number in dadu_array:
    if number == 2 or number == 6:
        length_of_dadu += 1


calculate_complement_not_2_6 = 1 - (length_of_dadu / default_dice_sample)
print(f"Kalkulasi Komplemen yang bukan 2 dan 6: {calculate_complement_not_2_6 * 100}%")

# Test 7
d2_trials = 2
d2_side = 6
d2_sample = d2_side ** d2_trials
summation = []
total = 0
len_of_val_7 = 0

dice_1 = []
dice_2 = []

d6_twice = 0
same_dice_twice = []

for d1 in range(1, d2_side + 1):
    for d2 in range(1, d2_side + 1):
        total = d1 + d2
        d6_twice = d1 == d2
        if total == 7:
            summation.append(total)
            len_of_val_7 = int(len(summation))
        if d1 == 6 and d2 == 6:
            same_dice_twice.append((d1, d2))

calculate_val_7 = 1 - (len_of_val_7 / d2_sample)
print(f"Kalkulasi Yang Dijumlahkan angka 7: {calculate_val_7 * 100}%")

# Test 8
default_set_card_hearth = 13

calculate_set_card_hearth = 1 - (default_set_card_hearth / default_set_card)
print(f"Kalkulasi Yang Bukan Hearth: {calculate_set_card_hearth * 100}%")

# Test 9
length_of_6_6 = len(same_dice_twice)
calculate_6_6 = 1 - (length_of_6_6 / d2_sample)
print(f"Kalkulasi yang tidak ada value 6,6 adalah: {calculate_6_6 * 100}%")

# Test 10

bola_merah = 4
bola_hijau = 3
bola_biru = 5

ruang_sampel = bola_merah + bola_hijau + bola_biru

print(ruang_sampel)

calculated = 1 - (4 / ruang_sampel)
print(f"Kalkulasi yang bukan bola merah: {calculated * 100}%")

# Test 11
c_trials = 2
c_side = 2
c_sample = c_side ** c_trials
length_of_image = 0
c_double_image = []

for c1 in range(1, c_side + 1):
    for c2 in range(1, c_side + 1):
        if c1 == 2 and c2 == 2:
            c_double_image.append((c1,c2))

length_of_image = len(c_double_image)

calculate_same_image = 1 - (length_of_image / c_sample)
print(f"Kalkulasi 2 gambar yang tidak akan muncul: {calculate_same_image * 100}%")

# Test 12
jumlah_siswa = 0
choosen_siswa = 1
siswa_laki_laki = 10
siswa_perempuan = 15

s_sample = (siswa_laki_laki + siswa_perempuan) ** choosen_siswa

calculate_choosen_siswa = 1 - (siswa_perempuan / s_sample)

print(f"Kalkulasi bukan Siswa Perempuan yang dipilih adalah: {calculate_choosen_siswa * 100}%")

P_EVENT = (6/15) / (10 / 15)

print(P_EVENT)

