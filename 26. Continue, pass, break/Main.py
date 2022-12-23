# continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak aakan dieksekusi

#angka = 0

#while angka < 5:
#        angka += 1

#        if angka == 3:
#                pass # ini tidk akan dieksesuki
        
#        print(angka)
#continue

angka = 0

print(F"angka sekarang -> {angka}")

while angka < 5:
        angka += 1 
        print(f"angka sekarang -> {angka}") # aksi 1

        if angka == 3:
                print("bagus")
                continue # akan membuat loop meloncat ke step selanjutnya

        print("apa kabar?") # aksi 1

print("Done")