# konversi suhu fahrenheit ke kelvin
fahrenheit = float(input("masukkan suhu dlm fahrenheit "))
print(fahrenheit, "fahrenheit")

kelvin  = (fahrenheit - 32) * (5/9) + 273.15
print(kelvin, "kelvin")

# Konversi suhu kelvin ke fahrenheit
fahrenheit = (kelvin - 273.15) * (9/5) + 32
print(fahrenheit, "fahrenheit")
