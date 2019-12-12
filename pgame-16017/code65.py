# Simpan dengan nama : code65.py
# Pemrograman Game Praktikum 6
# latihan code 6.5 : Fungsi / Function

# Contoh Fungsi 1, nama fungsi : myfungsi
def myfungsi():
	print("Ini dicetak dari myfungsi") # isi fungsi

# Contoh Fungsi 2, nama fungsi : my_fungsi
def my_fungsi():
	print("Ini dicetak dari my_fungsi") # isi fungsi


# Contoh Fungsi 3, nama fungsi : tambah_1
def tambah_1():
	print("t1 :", 4+4)

# Contoh Fungsi 4, nama fungsi : tambah_2
def tambah_2():
	a=4
	b=4
	print("t2 :", a+b)

# Contoh Fungsi 5, menggunakan parameter
def cetak_kata(kata):
	print("Kata yang dicetak :", kata)

# Memanggil Fungsi, caranya :
# tulis nama fungsi diikuti dengan "()"

myfungsi() 		# Memanggil Fungsi myfungsi
my_fungsi() 	# Memanggil Fungsi my_fungsi
tambah_1() 		# Memanggil Fungsi tambah_1
tambah_2() 		# Memanggil Fungsi tambah_2
# Memanggil Fungsi cetak_kata dengan parameter
cetak_kata("Hallo")