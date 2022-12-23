# Training untuk python

# -------0+++++++5-------8++++++11-------

inputUser = float(input("masukan angka yang bernilai\nkurang dari 0 \ndan \nlebih besar dari 10\n:"))

# ++++++3-------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# ---------10++++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# ++++++3---------10++++++

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan: ", isCorrect)