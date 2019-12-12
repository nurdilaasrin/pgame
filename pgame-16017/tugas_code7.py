a="Ini Merupakan Perulangan While"	# perulangan “while”
print(a)
x = 0
while (x < 5): 	# jika x lebih kecil dari 5 maka ulangi
# 	x = x + 1
	x += 1 			# x + 1
	print(" Nurdila Asrin ")

b="Ini Merupakan Perulangan For"	# perulangan “for”
print(b)
for x in range(5):
	print("Nurdila Asrin")

c="Ini Merupakan Fungsi / Function"	# Fungsi / Function
print(c)
# Fungsi / Function
def tambah_1(a,b):
	c = a + b
	print(c) # langsung cetak hasil

def tambah_2(a,b):
	c = a + b
	return c # mengembalikan nilai, disimpan dalam fungsi

# cara memanggil kedua fungsi tersebut
tambah_1(13,8)
print(tambah_2(43,8))

# memanggil fungsi dengan variable
a=24
b=26
tambah_1(a,b)
print(tambah_2(a,b))