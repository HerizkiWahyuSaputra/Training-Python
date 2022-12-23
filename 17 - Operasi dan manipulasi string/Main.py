# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case 
alay = "aKu KeCe AbieezZzZZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Okay"
cek_judul = judul.istitle() # hasil bool

print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith()
cek_start = "Haikyu Go".startswith("Haikyu")
print("start = " + str(cek_start))

cek_end = "Haikyu Go".endswith("Go")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['I','am','Human']
gabungan = ",".join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = "I am Human"
print(gabungan.split(' '))

# alokasi karakter rjust() ljust() center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(15,"+")
print("'"+tengah+"'") 

# kebalikannya -> strip()
tengah = tengah.strip("+") # menghilangkan tanda :
print("'"+tengah+"'")
