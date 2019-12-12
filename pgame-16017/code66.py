# Simpan dengan nama : code66.py
# Pemrograman Game Praktikum 6
# latihan code 6.6 : Fungsi / Function

# Contoh 1
def tambah_1(a,b):
	c = a + b
	print(c) # langsung cetak hasil

def tambah_2(a,b):
	c = a + b
	return c # mengembalikan nilai, disimpan dalam fungsi

# cara memanggil kedua fungsi tersebut
tambah_1(12,8)
print(tambah_2(22,8))

# memanggil fungsi dengan variable
a=24
b=26
tambah_1(a,b)
print(tambah_2(a,b))

# Contoh 2
# Penggunaan Variable global dan lokal
x = 100 	# variable global

def fungsi_1():
	x=10 	# variable local

# Mengubah variable global
def fungsi_2():
	global x # deklarasi variable global
	x=200# mengubah nilai variable global

fungsi_1() 	# panggil fungsi_1
print(x) 	# print x, berubah...?
fungsi_2() 	# Fungsi mengubah nilai variable global
print(x) 	# print x setelah diubah