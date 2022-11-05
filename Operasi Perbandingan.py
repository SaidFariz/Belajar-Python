# Operasi Perbandingan
'''
>, <, ==, !=, <=, >=, is, is not
Setiap hasilnya adalah boolean
'''

a = 9
b = 8 
print("a =", a,"|", "b =", b)

print("=== Lebih Dari (>) ===")
hasil = a > b 
print("a > b =", hasil)

print("=== Kurang Dari (<) ===")
hasil = a < b
print("a < b =", hasil)

print("=== Sama Dengan (=) ===")
hasil = a == b
print("a == b =", hasil)

print("=== Tidak Sama Dengan ===")
hasil = a != b
print("a != b =", hasil)

print("=== Lebih Dari atau Sama Dengan (>=) ===")
hasil = a >= b
print("a >= b =", hasil)

print("=== Kurang Dari atau Sama Dengan (<=) ===")
hasil = a <= b
print("a <= b =", hasil)

print("---- Operasi Identitas (is, is not) ----")

print("=== is ===") # logikanya seperti sama dengan
x = 9
y = 7
print("x =", x,"|", "y =", y)
hasil = x is y
print("x is y =", hasil)

x = 9
y = 9
print("x =", x,"|", "y =", y)
hasil = x is y
print("x is y =", hasil)

print("=== is not ===")# logikanya seperti tidak sama dengan
x = 9
y = 7
print("x =", x,"|", "y =", y)
hasil = x is not y
print("x is not y =", hasil)

x = 9
y = 9
print("x =", x,"|", "y =", y)
hasil = x is not y
print("x is not y =", hasil)

