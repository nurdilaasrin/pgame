# Simpan dengan nama : code61.py
# Pemrograman Game Praktikum 6
# latihan code 6 : Kondisional

# Buat variable untuk menampung inputan dari keyboard (user)
myvar=input("Masukkan Numerik atau String : ")

# kondisional if, else
# Memeriksa Variable dengan fungsi "snumeric()""
# kondisional if, else
if myvar.isnumeric():
	print("C1: Ya, Variable myvar Numerik : ", myvar)
else:
	pass
	# pass adalah perintah untuk abaikan

# print batas garis bintang
print('*'*25)

# kondisional if, elif
if not myvar.isnumeric():
	print("C2: Variable myvar BUKAN Numerik ! ")
elif myvar.isnumeric():
	print("C2: myvar : %s, adalah Numerik " % myvar) # cara 1
	print("C2: myvar : "+ myvar + ", adalah Numerik")# cara 2
	print("C2: myvar Numerik : ", myvar) # cara 3