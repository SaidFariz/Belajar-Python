print("=== Tipe Data Fundamental ===")
# angka tanpa koma (integer)
a = 10
print("nilai a =", a, type(a))

# angka dengan koma (float)
b = 7.1
print("nilai b =", b, type(b))


# kumpulan Karakter (string)
c = "Nganu"
print("nilai c =", c, type(c))

# biner true/ false (Boolean)
d = False
print("nilai d =", d, type(d))

print("=== Tipe data Khusus ===")
# tipe data complex
data = complex(9,6)
print("nilai data =", data, type(data))

# mengimpor data dari bahasa C
from ctypes import c_double, c_char
e = c_double(8.9)
print("nilai e =", e, type(e))