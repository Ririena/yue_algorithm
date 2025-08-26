# # ======================================================
# # Material Test: Complement Probability
# # Objective: To Simulate The Complement Event Probability
# # Language: Python
# # ======================================================
#
# pilih_objek = str(input("Pilih objek antara 'dadu'/'koin': "))
#
# if pilih_objek == "dadu":
#     trials = int(input("Berapa dadu yang mau di roll: "))
#     dice_side = 6
#     kalkulasi_sampel = dice_side ** trials
#     print(kalkulasi_sampel)
# elif pilih_objek == "koin":
#     trials = int(input("Berapa koin yang mau di lempar: "))
#     coin_side = 2
#     kalkulasi_sampel = coin_side ** trials
#
# calculating_complement = 1 - (1 / kalkulasi_sampel)
# print(calculating_complement * 100)

kartu_remi = 52
kartu_as = 4

peluang_kom_kartu = 1 - (4 / kartu_remi)
print(peluang_kom_kartu * 100)

dadu_side = [1,2,3,4,5,6]

for i in dadu_side:
    if i % 2 == 1:
        print(i)
