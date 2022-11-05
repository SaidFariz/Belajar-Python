# Operator logika

# Not, and, or, xor

print("=== Not ===")
var_a = False
var_b = not var_a
print("var_a = ", var_a)
print("--------------- NOT")
print("var_b = ", var_b)

print("=== And ===") # Ketika salah satu false maka hasilnya akan false (logikanya seperti operasi perkalian)
var_a = False
var_b = False
var_c = var_a and var_b
print(var_a, "and", var_b, "=", var_c)

var_a = False
var_b = True
var_c = var_a and var_b
print(var_a, "and", var_b, "=", var_c)

var_a = True
var_b = True
var_c = var_a and var_b
print(var_a, "and", var_b, "=", var_c)

var_a = True
var_b = False
var_c = var_a and var_b
print(var_a, "and", var_b, "=", var_c)

print("=== Or ===") # jika salah satu true maka hasilnya akan true (logikanya seperti operasi penjumlahan)
var_a = False
var_b = False
var_c = var_a or var_b
print(var_a, "or", var_b, "=", var_c)

var_a = True
var_b = True
var_c = var_a or var_b
print(var_a, "or", var_b, "=", var_c)

var_a = False
var_b = True
var_c = var_a or var_b
print(var_a, "or", var_b, "=", var_c)

var_a = True
var_b = False
var_c = var_a or var_b
print(var_a, "or", var_b, "=", var_c)

print("=== Xor ===") # Jika nilainya sama maka hasilnya akan sama (misal false ^ false = false)
var_a = False
var_b = False
var_c = var_a ^ var_b
print(var_a, "^", var_b, "=", var_c)

var_a = True
var_b = True
var_c = var_a ^ var_b
print(var_a, "^", var_b, "=", var_c)

var_a = True
var_b = False
var_c = var_a ^ var_b
print(var_a, "^", var_b, "=", var_c)

var_a = False
var_b = True
var_c = var_a ^ var_b
print(var_a, "^", var_b, "=", var_c)


