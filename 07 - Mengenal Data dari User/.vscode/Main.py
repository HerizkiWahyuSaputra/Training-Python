# Episode input user

# data yang dimasukan pasti string
data = input("Include data: ")

print("data = ",data,"type =", type(data))

# jika kita ingin mengambil ini, maka
number = float(input("masukan angka: "))
number = int(input("masukan angka: "))

print("data = ",number,",type =",type(number))

# bagaimana dengan boolean
biner = bool(int(input("masukan nilai boolean")))

print("data = ",biner,",type =",type(biner))