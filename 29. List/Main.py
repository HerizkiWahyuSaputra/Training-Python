## ---- LIST ----

# kumpulan data numbers
data_angka = [1,2,3,4,5]
print(data_angka)

# kumpulan data string
data_string = ["ucup", "reza", "dodo"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True]
print(data_boolean)

# kumpulan campuran
data_campuran = [1,"bala-bala",2,"bakwan",True,]
print(data_campuran)

## cara alternatif membuat list
data_range = range (0,10) # range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
data_list_use_for = [i**2 for i in range(0,15)]
print(data_list_use_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 ==0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 !=0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0,10) if i%2 ==0]
print(list_pake_for_if)
