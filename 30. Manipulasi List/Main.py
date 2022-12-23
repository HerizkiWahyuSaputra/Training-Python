## Operasi (Manipulasi List) 

# index   0      1      2
data = ["riz", "her", "iki"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_akhir = data[-1]
print(f"data terakhir adalah = {data_akhir}")

data_riz = data [-3]
print(f"data riz = {data_riz}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## Manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"putra") #(posisi,item)
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("Dudung") #(posisi,item)
print(f"data sesudah ditambah = \n{data}")

# menambah list dengan list
data_baru = ["ujang", "Asep", "wahyu"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data 2 menjadi michael
data[2] = "Michael"
print(f"data rubah = {data}")

# meremove data
data.remove("ujang")
print(f"data remove = {data}")

# meremove data paling belakang
data.pop()
print(f"data akhir = \n{data}")

print(data_akhir)