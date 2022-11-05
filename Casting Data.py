# Casting data/ Merubah data
# Tipe data  = Integer, Float, String, Boolean

print("=== INTEGER ===")
var_int = 2
print(var_int, type(var_int))
var_str =str(var_int)
var_float = float(var_int)
var_bool = bool(var_int)
print(var_str, type(var_str))
print(var_float, type(var_float))
print(var_bool, type(var_bool)) # akan false jika nilai = 0

print("=== FLOAT ===")
var_float = 9.9
print(var_float, type(var_float))
var_str = str(var_float)
var_bool = bool(var_float)
var_int = int(var_float) # akan dibulatkan kebawah

print(var_str, type(var_str))
print(var_bool, type(var_bool))
print(var_int, type(var_int))

print("=== STRING ===")
var_str = "0"
print(var_str, type(var_str))
var_bool = bool(var_str) # false jika string tidak diisi
var_int = int(var_str) # akan error jika nilainya bukan angka
var_float = float(var_str)

print(var_bool, type(var_bool))
print(var_int, type(var_int))
print(var_float, type(var_float))

print("=== BOOLEAN ===")
var_bool = False
print(var_bool, type(var_bool))
var_float= float(var_bool)
var_int = int(var_bool)
var_str = str(var_bool)
# Akan bernilai 0 saat false
print(var_float, type(var_float))
print(var_int, type(var_int))
print(var_str, type(var_str))
print("=== Akhir Program ===")