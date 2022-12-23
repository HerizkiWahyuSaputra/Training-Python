# Practice konversi satuan temperature

# program konversi celcius ke satuan lain

# FAHRENHEIT TEMPERATURE
print("FAHRENHEIT")

fahrenheit = float(input('masukan suhu dalam fahrenheit : '))
print("suhu adalah",fahrenheit, "fahrenheit")

# celcius
celcius = (5/9) * (fahrenheit - 32)
print("suhu dalam celcius adalah ",celcius, "celcius")

# reamur
reamur = (4/9) * (fahrenheit - 32)
print("suhu dalam reamur adalah ",reamur, "reamur")

# kelvin
kelvin = (5/9) * (fahrenheit - 32) + 273
print("suhu dalam kelvin adalah ",kelvin, "kelvin")

# KELVIN TEMPERATURE
print("KELVIN")

kelvin = float(input('masukan suhu dalam kelvin : '))
print("suhu adalah",kelvin, "kelvin")

# celcius
celcius = kelvin - 273
print("suhu dalam celcius adalah ",celcius, "celcius")

# reamur
reamur = (4/5) * (kelvin - 273)
print("suhu dalam reamur adalah ",reamur, "reamur")

# fahrenheit
kelvin = (9/5) * (kelvin - 273) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, "fahrenheit")