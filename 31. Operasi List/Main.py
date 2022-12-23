data_angka = [1,2,3,4,5,6,7,8,9,0,1,3,5,7,9,2,4,6,8]
print(f"data_angka = {data_angka}")

# count data (use in statistic)

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["Ucup","Dudung", "Ujang", "Jaka", "Raffi"]

print(f"data = {data}")

index_dudung = data.index("Dudung")
index_jaka = data.index("Jaka")
print(f"index si Dudung = {index_dudung}")
print(f"index si Dudung = {index_jaka}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sesudah sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")
