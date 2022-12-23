 # operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "Riz"
nama_tengah = "D"
nama_akhir = "Aen"

nama_lengkap = nama_pertama + " " + nama_tengah + "'"+ nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

D = "d"
status = d not in nama_lengkap
print(D + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-7 : " + nama_lengkap[7])
print("index ke-(-3) : " + nama_lengkap[-3])
print("index ke-(-5) : " + nama_lengkap[-5])
print("index ke-[0:3]: " + nama_lengkap[0:4])
print("index ke-[3:7]: " + nama_lengkap[3:8])
print("index ke-[0,2,4,6,8]: " + nama_lengkap[0:9:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 100
print("char untuk ASCII 100 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah)
)
