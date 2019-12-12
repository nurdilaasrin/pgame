# Simpan dengan nama : code62.py
# Pemrograman Game Praktikum 6
# latihan code 6.2 : Perulangan (Loop) while

batas='*'*30
# Contoh 1
x = 0
while (x < 5): # jika x lebih kecil dari 5 maka ulangi
# 	x = x + 1
	x += 1 # x + 1
	print(" Praktikum 6 no.", x)

print(batas)
# Contoh 2
# kombinasi while, if dan break
a = 0
while a < 6:
	print(" no a == ", a)
	if a == 3:# kondisional, jika sampai angka 3 maka
		break 	# berhenti perulangan
	a += 1

print(batas)
# Contoh 3
# kombinasi while, if dan continue
b = 0
while b < 6:
	b += 1
	if b == 3:
		print("B == ", b)
	continue # lanjutkan perulangan
	print(b)