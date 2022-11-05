'''
Membuat Operasi seperti ini
--> Masukkan angka
----0++++5----8++++11----
++++0----5++++8----11++++
'''

# Nomor 1
UsrInputs = float(input("Masukkan angka > 0 dan < 5 atau > 8 dan < 11 = "))
one = UsrInputs > 0
two = UsrInputs < 5
three = UsrInputs > 8
four = UsrInputs < 11
results = one and two or three and four
print(one, two, three, four)
print("Hasilnya adalah =", results) 

# Nomor 2
scan = float(input("Masukkan angka < 0 atau > 5 dan < 8 atau > 11 = "))
satu = scan < 0
dua = scan > 5
tiga = scan < 8
empat = scan > 11
results = satu or dua and tiga or empat
print(satu, dua, tiga, empat)
print("Hasilnya adalah =", results)
