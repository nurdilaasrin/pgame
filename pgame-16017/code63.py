# Simpan dengan nama : code63.py
# Pemrograman Game Praktikum 6
# latihan code 6.3 : Perulangan (Loop) while

batas='*'*30
# Contoh 4
# Penggunaan while dan else
c = 1
while c < 6:
	print("C == ",c)
	c += 1
else:
	print("batas c < 6")

print(batas)

# Contoh 5
# Penggunaan while dan list
buah = ["Apel", "Melon", "Durian"]
print("Buah 1: ",buah)
while buah:
	print("\tBuah: ",buah.pop())
print("Buah 2: ",buah)

print(batas)
# Contoh 6
n=10
while n > 0:
	print(n)
	n-= 1